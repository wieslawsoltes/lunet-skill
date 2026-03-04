#!/usr/bin/env python3
"""
Generate feature and public API references for the Lunet repository.

This script builds Lunet in Release mode, extracts exported API signatures
from each non-test top-level assembly, and writes feature/API reference files
for this skill.
"""

from __future__ import annotations

import argparse
import datetime as _dt
import json
import re
import shutil
import subprocess
import tempfile
import textwrap
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path


MODULE_DOC_MAP = {
    "ApiModule": "site/docs/plugins/api.md",
    "BundleModule": "site/docs/plugins/bundles.md",
    "ApiDotNetModule": "site/docs/plugins/api-dotnet.md",
    "MenuModule": "site/docs/plugins/menus.md",
    "ExtendsModule": "site/docs/plugins/extends.md",
    "SummarizerModule": "site/docs/plugins/summarizer.md",
    "MarkdownModule": "site/docs/plugins/markdown.md",
    "LayoutModule": "site/docs/layouts-and-includes.md",
    "ResourceModule": "site/docs/plugins/resources.md",
    "DatasModule": "site/docs/plugins/datas.md",
    "ServerModule": "site/docs/plugins/server.md",
    "WatcherModule": "site/docs/plugins/watcher.md",
    "MinifierModule": "site/docs/plugins/minifier.md",
    "RssModule": "site/docs/plugins/rss.md",
    "SassModule": "site/docs/plugins/scss.md",
    "TaxonomyModule": "site/docs/plugins/taxonomies.md",
    "CardsModule": "site/docs/plugins/cards.md",
    "SearchModule": "site/docs/plugins/search.md",
    "SitemapsModule": "site/docs/plugins/sitemaps.md",
    "AttributesModule": "site/docs/plugins/attributes.md",
    "YamlModule": "site/docs/plugins/yaml.md",
    "JsonModule": "site/docs/plugins/json.md",
    "TomlModule": "site/docs/plugins/toml.md",
    "TrackingModule": "site/docs/plugins/tracking.md",
}

EXCLUDED_PROJECTS = {"Lunet.Tests", "Lunet.Api.DotNet.Extractor.CodeGen"}
DEFAULT_TARGET_FRAMEWORK = "net10.0"


@dataclass(frozen=True)
class ProjectInfo:
    name: str
    assembly_name: str
    target_framework: str
    csproj_path: Path


def _run(cmd: list[str], cwd: Path) -> None:
    subprocess.run(cmd, cwd=cwd, check=True)


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _tag_name(element: ET.Element) -> str:
    return element.tag.split("}", 1)[-1]


def _read_csproj_metadata(csproj_path: Path) -> ProjectInfo:
    tree = ET.parse(csproj_path)
    root = tree.getroot()

    assembly_name = None
    target_framework = None
    target_frameworks = None

    for element in root.iter():
        tag = _tag_name(element)
        if tag == "AssemblyName" and element.text:
            assembly_name = element.text.strip()
        elif tag == "TargetFramework" and element.text:
            target_framework = element.text.strip()
        elif tag == "TargetFrameworks" and element.text:
            target_frameworks = element.text.strip()

    if target_framework is None and target_frameworks:
        target_framework = target_frameworks.split(";", 1)[0].strip()

    if not target_framework:
        target_framework = DEFAULT_TARGET_FRAMEWORK

    project_name = csproj_path.stem
    return ProjectInfo(
        name=project_name,
        assembly_name=assembly_name or project_name,
        target_framework=target_framework,
        csproj_path=csproj_path,
    )


def _discover_projects(repo_root: Path) -> list[ProjectInfo]:
    src_dir = repo_root / "src"
    projects: list[ProjectInfo] = []
    for csproj in sorted(src_dir.glob("*/*.csproj")):
        project = _read_csproj_metadata(csproj)
        if project.name in EXCLUDED_PROJECTS:
            continue
        projects.append(project)
    return projects


def _find_assembly_path(project: ProjectInfo) -> Path:
    project_dir = project.csproj_path.parent
    preferred = (
        project_dir
        / "bin"
        / "Release"
        / project.target_framework
        / f"{project.assembly_name}.dll"
    )
    if preferred.exists():
        return preferred

    candidates = sorted(
        project_dir.glob(f"bin/Release/**/{project.assembly_name}.dll"),
        key=lambda p: ("/ref/" in str(p).replace("\\", "/"), len(str(p))),
    )
    for candidate in candidates:
        if "/ref/" not in str(candidate).replace("\\", "/"):
            return candidate

    raise FileNotFoundError(
        f"Unable to locate assembly for {project.name} "
        f"({project.assembly_name}.dll) after build."
    )


def _ensure_assembly_path(repo_root: Path, project: ProjectInfo) -> Path | None:
    try:
        return _find_assembly_path(project)
    except FileNotFoundError:
        # Some projects are not in src/lunet.slnx (e.g. ApiExample); build on demand.
        _run(
            [
                "dotnet",
                "build",
                "-c",
                "Release",
                str(project.csproj_path.relative_to(repo_root)),
            ],
            repo_root,
        )
        try:
            return _find_assembly_path(project)
        except FileNotFoundError:
            print(
                f"[WARN] Skipping project without build output: {project.name} ({project.csproj_path})"
            )
            return None


def _extract_modules(lunet_app_path: Path) -> list[str]:
    text = _read_text(lunet_app_path)
    list_match = re.search(
        r"Modules\s*=\s*new\s+OrderedList<SiteModule>\s*\(\)\s*\{(?P<body>.*?)\};",
        text,
        re.DOTALL,
    )
    if not list_match:
        return []
    body = list_match.group("body")
    return re.findall(r"new\s+([A-Za-z0-9_]+)\s*\(\s*\)\s*,", body)


def _discover_module_definitions(repo_root: Path) -> dict[str, tuple[str, Path]]:
    module_pattern = re.compile(
        r"public\s+class\s+(?P<module>[A-Za-z0-9_]+)\s*:\s*SiteModule(?:<(?P<plugin>[A-Za-z0-9_]+)>)?"
    )
    definitions: dict[str, tuple[str, Path]] = {}
    for file_path in sorted((repo_root / "src").glob("**/*.cs")):
        if "/Lunet.Tests/" in str(file_path):
            continue
        text = _read_text(file_path)
        for match in module_pattern.finditer(text):
            module_name = match.group("module")
            plugin_name = match.group("plugin") or "-"
            definitions[module_name] = (plugin_name, file_path)
    return definitions


def _extract_frontmatter_title(markdown_path: Path) -> str:
    text = _read_text(markdown_path)
    match = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if match:
        frontmatter = match.group(1)
        title_match = re.search(r"^title:\s*\"?(.*?)\"?\s*$", frontmatter, re.MULTILINE)
        if title_match:
            return title_match.group(1).strip()

    heading_match = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
    if heading_match:
        return heading_match.group(1).strip()

    return markdown_path.stem


def _extract_readme_features(readme_path: Path) -> list[str]:
    text = _read_text(readme_path)
    section = re.search(r"##\s*✨\s*Features\s*(.*?)\n##\s", text, re.DOTALL)
    if not section:
        return []
    body = section.group(1)
    features = []
    for line in body.splitlines():
        line = line.strip()
        if line.startswith("- "):
            features.append(line[2:].strip())
    return features


def _write_feature_reference(
    repo_root: Path,
    projects: list[ProjectInfo],
    output_path: Path,
) -> None:
    modules = _extract_modules(repo_root / "src" / "Lunet.Application" / "LunetApp.cs")
    module_defs = _discover_module_definitions(repo_root)
    features = _extract_readme_features(repo_root / "readme.md")

    docs_files = sorted(
        p
        for p in (repo_root / "site" / "docs").glob("**/*.md")
        if "/todos/" not in str(p).replace("\\", "/")
    )

    project_by_name = {project.name: project for project in projects}

    lines: list[str] = []
    lines.append("# Lunet Feature Reference")
    lines.append("")
    lines.append(
        f"Generated from repository sources on {_dt.datetime.now().isoformat(timespec='seconds')}."
    )
    lines.append("")

    if features:
        lines.append("## Product Features (readme.md)")
        lines.append("")
        for item in features:
            lines.append(f"- {item}")
        lines.append("")

    lines.append("## Plugin Registration Order (LunetApp.Modules)")
    lines.append("")
    lines.append("| # | Module | Plugin | Project | Docs | Source |")
    lines.append("|---|---|---|---|---|---|")

    for index, module in enumerate(modules, start=1):
        plugin_name, source_path = module_defs.get(module, ("-", Path("-")))
        source_rel = source_path.relative_to(repo_root) if source_path != Path("-") else Path("-")
        docs_rel = MODULE_DOC_MAP.get(module, "-")

        project_name = "-"
        if source_path != Path("-"):
            parts = source_rel.parts
            if len(parts) >= 2:
                candidate = parts[1]
                if candidate in project_by_name:
                    project_name = candidate
                else:
                    # Some folders do not equal csproj stem (e.g. Lunet.Markdig -> Lunet.Markdown)
                    project_name = next(
                        (
                            project.name
                            for project in projects
                            if str(project.csproj_path.parent.relative_to(repo_root / "src")) == candidate
                        ),
                        candidate,
                    )

        docs_cell = f"`{docs_rel}`" if docs_rel != "-" else "-"
        lines.append(
            f"| {index} | `{module}` | `{plugin_name}` | `{project_name}` | {docs_cell} | `{source_rel}` |"
        )

    lines.append("")
    lines.append("## Documentation Pages")
    lines.append("")
    lines.append("| Path | Title |")
    lines.append("|---|---|")
    for doc in docs_files:
        rel = doc.relative_to(repo_root)
        title = _extract_frontmatter_title(doc).replace("|", "\\|")
        lines.append(f"| `{rel}` | {title} |")

    lines.append("")
    lines.append("## Project and Assembly Map")
    lines.append("")
    lines.append("| Project | Assembly | TargetFramework | csproj |")
    lines.append("|---|---|---|---|")
    for project in projects:
        rel = project.csproj_path.relative_to(repo_root)
        lines.append(
            f"| `{project.name}` | `{project.assembly_name}` | `{project.target_framework}` | `{rel}` |"
        )

    lines.append("")
    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _create_inspector_source() -> str:
    return textwrap.dedent(
        r"""
        using System;
        using System.Collections.Generic;
        using System.IO;
        using System.Linq;
        using System.Reflection;
        using System.Runtime.CompilerServices;
        using System.Text;
        using System.Text.Json;

        public sealed class AssemblySummary
        {
            public string Name { get; set; } = "";
            public string FileName { get; set; } = "";
            public string AssemblyPath { get; set; } = "";
            public int TypeCount { get; set; }
            public int MemberCount { get; set; }
        }

        public static class Program
        {
            public static int Main(string[] args)
            {
                if (args.Length < 2)
                {
                    Console.Error.WriteLine("Usage: ApiInspector <output-dir> <assembly-path> [assembly-path...]");
                    return 1;
                }

                var outputDir = args[0];
                var assemblyPaths = args.Skip(1).Select(Path.GetFullPath).Distinct(StringComparer.OrdinalIgnoreCase).ToArray();
                Directory.CreateDirectory(outputDir);

                var resolverMap = BuildResolverMap(assemblyPaths);
                AppDomain.CurrentDomain.AssemblyResolve += (_, eventArgs) =>
                {
                    var shortName = new AssemblyName(eventArgs.Name).Name ?? "";
                    if (resolverMap.TryGetValue(shortName, out var path))
                    {
                        try { return Assembly.LoadFrom(path); } catch { return null; }
                    }
                    return null;
                };

                var summaries = new List<AssemblySummary>();

                foreach (var assemblyPath in assemblyPaths)
                {
                    if (!File.Exists(assemblyPath))
                    {
                        Console.Error.WriteLine($"[WARN] Assembly not found: {assemblyPath}");
                        continue;
                    }

                    Assembly assembly;
                    try
                    {
                        assembly = Assembly.LoadFrom(assemblyPath);
                    }
                    catch (Exception ex)
                    {
                        Console.Error.WriteLine($"[WARN] Failed to load {assemblyPath}: {ex.Message}");
                        continue;
                    }

                    var assemblyName = assembly.GetName().Name ?? Path.GetFileNameWithoutExtension(assemblyPath);
                    var fileName = SanitizeFileName(assemblyName) + ".md";
                    var outputPath = Path.Combine(outputDir, fileName);

                    int typeCount;
                    int memberCount;
                    try
                    {
                        WriteAssemblyReference(outputPath, assembly, assemblyPath, out typeCount, out memberCount);
                    }
                    catch (Exception ex)
                    {
                        typeCount = 0;
                        memberCount = 0;
                        File.WriteAllText(
                            outputPath,
                            $"# {assemblyName} Public API\n\n" +
                            $"Assembly path: `{assemblyPath}`\n\n" +
                            $"API extraction failed: `{ex.GetType().FullName}` - {ex.Message}\n"
                        );
                        Console.Error.WriteLine($"[WARN] API extraction failed for {assemblyPath}: {ex.Message}");
                    }

                    summaries.Add(new AssemblySummary
                    {
                        Name = assemblyName,
                        FileName = fileName,
                        AssemblyPath = assemblyPath,
                        TypeCount = typeCount,
                        MemberCount = memberCount,
                    });
                }

                summaries = summaries
                    .OrderBy(x => x.Name, StringComparer.Ordinal)
                    .ToList();

                var summaryPath = Path.Combine(outputDir, "summary.json");
                File.WriteAllText(summaryPath, JsonSerializer.Serialize(
                    summaries,
                    new JsonSerializerOptions { WriteIndented = true }
                ));

                return 0;
            }

            private static Dictionary<string, string> BuildResolverMap(IEnumerable<string> assemblyPaths)
            {
                var map = new Dictionary<string, (Version Version, string Path)>(StringComparer.OrdinalIgnoreCase);

                static void AddDirectory(
                    string? directory,
                    SearchOption searchOption,
                    Dictionary<string, (Version Version, string Path)> map)
                {
                    if (string.IsNullOrWhiteSpace(directory) || !Directory.Exists(directory))
                    {
                        return;
                    }

                    foreach (var dll in Directory.EnumerateFiles(directory, "*.dll", searchOption))
                    {
                        try
                        {
                            var asmName = AssemblyName.GetAssemblyName(dll);
                            var shortName = asmName.Name;
                            if (string.IsNullOrWhiteSpace(shortName))
                            {
                                continue;
                            }

                            var version = asmName.Version ?? new Version(0, 0, 0, 0);
                            if (map.TryGetValue(shortName, out var existing) && existing.Version >= version)
                            {
                                continue;
                            }

                            map[shortName] = (version, dll);
                        }
                        catch
                        {
                            // Ignore native/invalid files
                        }
                    }
                }

                foreach (var path in assemblyPaths)
                {
                    AddDirectory(Path.GetDirectoryName(path), SearchOption.TopDirectoryOnly, map);
                }

                foreach (var path in assemblyPaths)
                {
                    AddDirectory(Path.GetDirectoryName(path), SearchOption.AllDirectories, map);
                }

                var nugetPackages = Environment.GetEnvironmentVariable("NUGET_PACKAGES");
                if (string.IsNullOrWhiteSpace(nugetPackages))
                {
                    var home = Environment.GetFolderPath(Environment.SpecialFolder.UserProfile);
                    if (!string.IsNullOrWhiteSpace(home))
                    {
                        nugetPackages = Path.Combine(home, ".nuget", "packages");
                    }
                }

                if (!string.IsNullOrWhiteSpace(nugetPackages) && Directory.Exists(nugetPackages))
                {
                    foreach (var packageDir in Directory.EnumerateDirectories(nugetPackages))
                    {
                        foreach (var versionDir in Directory.EnumerateDirectories(packageDir))
                        {
                            AddDirectory(Path.Combine(versionDir, "lib"), SearchOption.AllDirectories, map);
                            AddDirectory(Path.Combine(versionDir, "tools"), SearchOption.AllDirectories, map);
                        }
                    }
                }

                return map.ToDictionary(pair => pair.Key, pair => pair.Value.Path, StringComparer.OrdinalIgnoreCase);
            }

            private static void WriteAssemblyReference(
                string outputPath,
                Assembly assembly,
                string assemblyPath,
                out int typeCount,
                out int memberCount)
            {
                var exportedTypes = GetExportedTypesSafe(assembly)
                    .OrderBy(t => t.FullName, StringComparer.Ordinal)
                    .ToList();

                typeCount = exportedTypes.Count;
                memberCount = 0;

                using var writer = new StreamWriter(outputPath, false, new UTF8Encoding(false));
                writer.WriteLine($"# {assembly.GetName().Name} Public API");
                writer.WriteLine();
                writer.WriteLine($"Assembly path: `{assemblyPath}`");
                writer.WriteLine();
                writer.WriteLine($"Exported types: **{typeCount}**");
                writer.WriteLine();
                writer.WriteLine("## Types");
                writer.WriteLine();

                foreach (var type in exportedTypes)
                {
                    var typeDisplay = FormatType(type);
                    writer.WriteLine($"### `{typeDisplay}`");
                    writer.WriteLine();
                    writer.WriteLine($"- Kind: `{GetTypeKind(type)}`");

                    if (type.BaseType is not null && type.BaseType != typeof(object) && !type.IsInterface && !type.IsEnum)
                    {
                        writer.WriteLine($"- Base: `{FormatType(type.BaseType)}`");
                    }

                    var interfaces = type.GetInterfaces()
                        .Select(FormatType)
                        .Distinct(StringComparer.Ordinal)
                        .OrderBy(x => x, StringComparer.Ordinal)
                        .ToList();
                    if (interfaces.Count > 0)
                    {
                        writer.WriteLine($"- Interfaces: `{string.Join("`, `", interfaces)}`");
                    }

                    var constructors = type.GetConstructors(BindingFlags.Public | BindingFlags.Instance | BindingFlags.Static | BindingFlags.DeclaredOnly)
                        .Select(FormatMethodBase)
                        .OrderBy(x => x, StringComparer.Ordinal)
                        .ToList();

                    var methods = type.GetMethods(BindingFlags.Public | BindingFlags.Instance | BindingFlags.Static | BindingFlags.DeclaredOnly)
                        .Where(m => !m.IsSpecialName || m.Name.StartsWith("op_", StringComparison.Ordinal))
                        .Select(FormatMethodInfo)
                        .OrderBy(x => x, StringComparer.Ordinal)
                        .ToList();

                    var properties = type.GetProperties(BindingFlags.Public | BindingFlags.Instance | BindingFlags.Static | BindingFlags.DeclaredOnly)
                        .Select(FormatPropertyInfo)
                        .OrderBy(x => x, StringComparer.Ordinal)
                        .ToList();

                    var fields = type.GetFields(BindingFlags.Public | BindingFlags.Instance | BindingFlags.Static | BindingFlags.DeclaredOnly)
                        .Select(FormatFieldInfo)
                        .OrderBy(x => x, StringComparer.Ordinal)
                        .ToList();

                    var events = type.GetEvents(BindingFlags.Public | BindingFlags.Instance | BindingFlags.Static | BindingFlags.DeclaredOnly)
                        .Select(FormatEventInfo)
                        .OrderBy(x => x, StringComparer.Ordinal)
                        .ToList();

                    memberCount += constructors.Count + methods.Count + properties.Count + fields.Count + events.Count;

                    WriteSection(writer, "Constructors", constructors);
                    WriteSection(writer, "Methods", methods);
                    WriteSection(writer, "Properties", properties);
                    WriteSection(writer, "Fields", fields);
                    WriteSection(writer, "Events", events);
                }
            }

            private static void WriteSection(StreamWriter writer, string title, IReadOnlyList<string> items)
            {
                if (items.Count == 0)
                {
                    return;
                }

                writer.WriteLine();
                writer.WriteLine($"#### {title}");
                writer.WriteLine();
                foreach (var item in items)
                {
                    writer.WriteLine($"- `{item}`");
                }
            }

            private static IEnumerable<Type> GetExportedTypesSafe(Assembly assembly)
            {
                try
                {
                    return assembly.GetExportedTypes();
                }
                catch (ReflectionTypeLoadException ex)
                {
                    return ex.Types.Where(t => t is not null).Cast<Type>();
                }
                catch
                {
                    return Array.Empty<Type>();
                }
            }

            private static string GetTypeKind(Type type)
            {
                if (type.IsInterface) return "interface";
                if (type.IsEnum) return "enum";
                if (type.IsValueType && !type.IsPrimitive) return type.IsByRefLike ? "ref struct" : "struct";
                if (type.IsClass && type.IsAbstract && type.IsSealed) return "static class";
                if (type.IsClass && type.IsAbstract) return "abstract class";
                if (type.IsClass) return "class";
                return "type";
            }

            private static string FormatMethodBase(MethodBase method)
            {
                var genericSuffix = "";
                if (method is MethodInfo methodInfo && methodInfo.IsGenericMethodDefinition)
                {
                    var genericArgs = methodInfo.GetGenericArguments().Select(a => a.Name);
                    genericSuffix = "<" + string.Join(", ", genericArgs) + ">";
                }

                var modifiers = new List<string>();
                if (method.IsStatic) modifiers.Add("static");
                if (method.IsAbstract) modifiers.Add("abstract");
                if (method.IsVirtual && !method.IsAbstract) modifiers.Add("virtual");

                var parameters = string.Join(", ", method.GetParameters().Select(FormatParameterInfo));
                var typeName = method.DeclaringType is null ? "ctor" : GetSimpleTypeName(method.DeclaringType);
                var memberName = method.IsConstructor ? typeName : method.Name.Split('`')[0] + genericSuffix;

                return $"{string.Join(" ", modifiers)} {memberName}({parameters})".Trim();
            }

            private static string FormatMethodInfo(MethodInfo method)
            {
                var returnType = FormatType(method.ReturnType);
                return $"{returnType} {FormatMethodBase(method)}";
            }

            private static string FormatPropertyInfo(PropertyInfo property)
            {
                var getter = property.GetMethod;
                var setter = property.SetMethod;

                var accessors = new List<string>();
                if (getter is not null && getter.IsPublic) accessors.Add("get;");
                if (setter is not null && setter.IsPublic) accessors.Add("set;");

                var indexParameters = property.GetIndexParameters();
                var indexSuffix = "";
                if (indexParameters.Length > 0)
                {
                    var formatted = string.Join(", ", indexParameters.Select(FormatParameterInfo));
                    indexSuffix = $"[{formatted}]";
                }

                return $"{FormatType(property.PropertyType)} {property.Name}{indexSuffix} {{ {string.Join(" ", accessors)} }}";
            }

            private static string FormatFieldInfo(FieldInfo field)
            {
                var modifiers = new List<string>();
                if (field.IsLiteral) modifiers.Add("const");
                else if (field.IsInitOnly) modifiers.Add("readonly");
                if (field.IsStatic) modifiers.Add("static");
                return $"{string.Join(" ", modifiers)} {FormatType(field.FieldType)} {field.Name}".Trim();
            }

            private static string FormatEventInfo(EventInfo eventInfo)
            {
                return $"{FormatType(eventInfo.EventHandlerType ?? typeof(void))} {eventInfo.Name}";
            }

            private static string FormatParameterInfo(ParameterInfo parameter)
            {
                var prefix = "";
                var parameterType = parameter.ParameterType;

                if (parameter.IsOut)
                {
                    prefix = "out ";
                    parameterType = parameterType.GetElementType() ?? parameterType;
                }
                else if (parameterType.IsByRef)
                {
                    prefix = "ref ";
                    parameterType = parameterType.GetElementType() ?? parameterType;
                }
                else if (parameter.IsDefined(typeof(ParamArrayAttribute), inherit: false))
                {
                    prefix = "params ";
                }

                var optional = parameter.IsOptional ? " = optional" : "";
                var name = string.IsNullOrWhiteSpace(parameter.Name) ? "value" : parameter.Name!;
                return $"{prefix}{FormatType(parameterType)} {name}{optional}";
            }

            private static string FormatType(Type type)
            {
                if (type.IsGenericParameter) return type.Name;

                if (type.IsByRef)
                {
                    return $"{FormatType(type.GetElementType()!)}&";
                }

                if (type.IsPointer)
                {
                    return $"{FormatType(type.GetElementType()!)}*";
                }

                if (type.IsArray)
                {
                    var commas = new string(',', type.GetArrayRank() - 1);
                    return $"{FormatType(type.GetElementType()!)}[{commas}]";
                }

                if (type.IsGenericType)
                {
                    var definitionName = (type.GetGenericTypeDefinition().FullName ?? type.Name)
                        .Split('`')[0]
                        .Replace('+', '.');
                    var args = type.GetGenericArguments().Select(FormatType);
                    return $"{definitionName}<{string.Join(", ", args)}>";
                }

                return (type.FullName ?? type.Name).Replace('+', '.');
            }

            private static string GetSimpleTypeName(Type type)
            {
                var name = type.Name;
                var tick = name.IndexOf('`');
                return tick >= 0 ? name[..tick] : name;
            }

            private static string SanitizeFileName(string value)
            {
                foreach (var c in Path.GetInvalidFileNameChars())
                {
                    value = value.Replace(c, '-');
                }
                return value;
            }
        }
        """
    ).strip() + "\n"


def _run_api_inspector(assemblies: list[Path], api_output_dir: Path) -> list[dict]:
    with TemporaryDirectoryPath() as temp_dir:
        csproj_path = temp_dir / "ApiInspector.csproj"
        program_path = temp_dir / "Program.cs"

        csproj_path.write_text(
            textwrap.dedent(
                """
                <Project Sdk="Microsoft.NET.Sdk">
                  <PropertyGroup>
                    <OutputType>Exe</OutputType>
                    <TargetFramework>net10.0</TargetFramework>
                    <ImplicitUsings>enable</ImplicitUsings>
                    <Nullable>enable</Nullable>
                  </PropertyGroup>
                </Project>
                """
            ).strip()
            + "\n",
            encoding="utf-8",
        )
        program_path.write_text(_create_inspector_source(), encoding="utf-8")

        cmd = [
            "dotnet",
            "run",
            "--project",
            str(csproj_path),
            "--configuration",
            "Release",
            "--",
            str(api_output_dir),
            *[str(path) for path in assemblies],
        ]
        _run(cmd, temp_dir)

    summary_path = api_output_dir / "summary.json"
    if not summary_path.exists():
        raise FileNotFoundError(f"API summary was not generated: {summary_path}")
    return json.loads(summary_path.read_text(encoding="utf-8"))


def _to_repo_relative_str(path: Path, repo_root: Path) -> str:
    try:
        return str(path.resolve().relative_to(repo_root.resolve())).replace("\\", "/")
    except ValueError:
        return path.name


def _sanitize_generated_paths(
    repo_root: Path,
    projects: list[ProjectInfo],
    summary: list[dict],
    api_dir: Path,
) -> list[dict]:
    repo_root_resolved = repo_root.resolve()
    repo_root_text = str(repo_root_resolved)

    per_assembly_replacements: dict[str, str] = {}
    for item in summary:
        raw_path = item.get("AssemblyPath")
        if not isinstance(raw_path, str) or not raw_path:
            continue
        old_path = raw_path
        new_path = _to_repo_relative_str(Path(raw_path), repo_root)
        item["AssemblyPath"] = new_path
        per_assembly_replacements[old_path] = new_path

    project_replacements: dict[str, str] = {}
    for project in projects:
        project_root = project.csproj_path.parent.resolve()
        project_replacements[str(project_root)] = _to_repo_relative_str(project_root, repo_root)

    for api_file in sorted(api_dir.glob("*.md")):
        text = _read_text(api_file)

        for old_path, new_path in per_assembly_replacements.items():
            text = text.replace(f"Assembly path: `{old_path}`", f"Assembly path: `{new_path}`")
            text = text.replace(old_path, new_path)

        for old_path, new_path in project_replacements.items():
            text = text.replace(old_path, new_path)

        # Last defensive cleanup to avoid leaking machine-local paths.
        text = text.replace(repo_root_text, "<repo-root>")

        api_file.write_text(text, encoding="utf-8")

    return summary


class TemporaryDirectoryPath:
    def __init__(self) -> None:
        self._path: Path | None = None

    def __enter__(self) -> Path:
        self._path = Path(tempfile.mkdtemp(prefix="lunet-api-ref-"))
        return self._path

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        if self._path and self._path.exists():
            shutil.rmtree(self._path, ignore_errors=True)


TYPE_DECLARATION_RE = re.compile(
    r"^public\s+(?:[A-Za-z_][A-Za-z0-9_]*\s+)*(class|struct|interface|enum|record|delegate)\b"
)


def _try_source_api_fallback(project: ProjectInfo, assembly_name: str, assembly_path: str, api_file: Path) -> tuple[int, int]:
    root = project.csproj_path.parent
    file_entries: dict[str, dict[str, list[str]]] = {}
    type_count = 0
    member_count = 0

    for source in sorted(root.glob("**/*.cs")):
        rel = source.relative_to(root)
        if "bin" in rel.parts or "obj" in rel.parts:
            continue
        if source.name.endswith(".g.cs"):
            continue

        types: list[str] = []
        members: list[str] = []
        for raw_line in _read_text(source).splitlines():
            line = " ".join(raw_line.strip().split())
            if not line.startswith("public "):
                continue

            if TYPE_DECLARATION_RE.match(line):
                types.append(line)
            else:
                members.append(line)

        if types or members:
            file_entries[str(rel)] = {"types": types, "members": members}
            type_count += len(types)
            member_count += len(members)

    # Only fallback when we can identify at least one public type declaration.
    # Public members on non-public types are not part of the assembly public API.
    if type_count == 0:
        return 0, 0

    lines: list[str] = []
    lines.append(f"# {assembly_name} Public API (Source Fallback)")
    lines.append("")
    lines.append(f"Assembly path: `{assembly_path}`")
    lines.append("")
    lines.append(
        "Reflection-based extraction returned no exported types for this assembly. "
        "The reference below is generated from source-level public declarations."
    )
    lines.append("")
    lines.append(f"- Source root: `{root}`")
    lines.append(f"- Public type declarations: **{type_count}**")
    lines.append(f"- Other public declarations: **{member_count}**")
    lines.append("")

    for rel in sorted(file_entries):
        entry = file_entries[rel]
        lines.append(f"## `{rel}`")
        lines.append("")
        if entry["types"]:
            lines.append("### Types")
            lines.append("")
            for item in entry["types"]:
                lines.append(f"- `{item}`")
            lines.append("")
        if entry["members"]:
            lines.append("### Members")
            lines.append("")
            for item in entry["members"]:
                lines.append(f"- `{item}`")
            lines.append("")

    api_file.write_text("\n".join(lines), encoding="utf-8")
    return type_count, member_count


def _apply_source_fallbacks(
    projects: list[ProjectInfo],
    summary: list[dict],
    api_dir: Path,
) -> list[dict]:
    project_by_assembly = {project.assembly_name: project for project in projects}
    for item in summary:
        if item.get("TypeCount", 0) != 0:
            continue

        assembly_name = item.get("Name", "")
        project = project_by_assembly.get(assembly_name)
        if project is None:
            continue

        file_name = item.get("FileName", "")
        assembly_path = item.get("AssemblyPath", "")
        if not file_name or not assembly_path:
            continue

        api_file = api_dir / file_name
        type_count, member_count = _try_source_api_fallback(
            project,
            assembly_name,
            assembly_path,
            api_file,
        )
        if type_count > 0:
            item["TypeCount"] = type_count
            item["MemberCount"] = member_count

    return summary


def _write_public_api_index(
    repo_root: Path,
    output_path: Path,
    summary: list[dict],
) -> None:
    total_types = sum(item.get("TypeCount", 0) for item in summary)
    total_members = sum(item.get("MemberCount", 0) for item in summary)

    lines: list[str] = []
    lines.append("# Lunet Public API Index")
    lines.append("")
    lines.append(
        f"Generated from built assemblies on {_dt.datetime.now().isoformat(timespec='seconds')}."
    )
    lines.append("")
    lines.append(f"- Assemblies: **{len(summary)}**")
    lines.append(f"- Exported types: **{total_types}**")
    lines.append(f"- Public members (declared): **{total_members}**")
    lines.append("")
    lines.append("| Assembly | Types | Members | Reference | Built DLL |")
    lines.append("|---|---:|---:|---|---|")

    for item in sorted(summary, key=lambda entry: entry["Name"]):
        assembly = item["Name"]
        file_name = item["FileName"]
        type_count = item["TypeCount"]
        member_count = item["MemberCount"]
        dll_path = Path(item["AssemblyPath"])
        try:
            dll_rel = dll_path.relative_to(repo_root)
        except ValueError:
            dll_rel = dll_path
        lines.append(
            f"| `{assembly}` | {type_count} | {member_count} | `references/api/{file_name}` | `{dll_rel}` |"
        )

    lines.append("")
    lines.append("## Search Patterns")
    lines.append("")
    lines.append(
        "- `rg -n \"SiteObject|SiteRunner|SiteApplication\" references/api/*.md`"
    )
    lines.append("- `rg -n \"ApiDotNet|ApiModule|ApiPlugin\" references/api/*.md`")
    lines.append("- `rg -n \"Bundle|Layout|Markdown|Search\" references/api/*.md`")
    lines.append("- `rg -n \"DartSass|Resource|Taxonomy|Tracking\" references/api/*.md`")
    lines.append("")
    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _write_repo_entry_reference(repo_root: Path, output_path: Path) -> None:
    lines = [
        "# Lunet Build and Documentation Workflow",
        "",
        "## Local Build + Test",
        "",
        "Run from repository root:",
        "",
        "```bash",
        "cd src",
        "dotnet build -c Release",
        "dotnet test -c Release",
        "```",
        "",
        "## Build Site with Local Lunet",
        "",
        "```bash",
        "cd site",
        "dotnet ../src/Lunet/bin/Release/net10.0/lunet.dll --stacktrace build --dev",
        "```",
        "",
        "## Key Entry Points",
        "",
        "- `readme.md`",
        "- `site/docs/readme.md`",
        "- `site/architecture.md`",
        "- `src/Lunet.Application/LunetApp.cs`",
        "- `src/Lunet.Core/Core/SiteObject.cs`",
        "- `src/Lunet.Core/Core/ContentPlugin.cs`",
        "- `src/Lunet.Core/Core/SiteApplication.cs`",
        "",
        "## Plugin Docs Root",
        "",
        "- `site/docs/plugins/readme.md`",
        "",
        "## API Docs Feature",
        "",
        "- `site/docs/plugins/api.md`",
        "- `site/docs/plugins/api-dotnet.md`",
        "- `src/Lunet.Api/Lunet.Api.csproj`",
        "- `src/Lunet.Api.DotNet/Lunet.Api.DotNet.csproj`",
        "- `src/Lunet.Api.DotNet.Extractor/Lunet.Api.DotNet.Extractor.csproj`",
        "",
    ]
    output_path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate Lunet skill references.")
    parser.add_argument("--repo", required=True, help="Path to Lunet repository root.")
    parser.add_argument(
        "--output",
        required=True,
        help="Output references directory (typically <skill>/references).",
    )
    parser.add_argument(
        "--skip-build",
        action="store_true",
        help="Skip `dotnet build -c Release src/lunet.slnx`.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo_root = Path(args.repo).resolve()
    output_dir = Path(args.output).resolve()

    if not (repo_root / "src" / "lunet.slnx").exists():
        raise FileNotFoundError(
            f"Expected Lunet solution at {repo_root / 'src' / 'lunet.slnx'}"
        )

    output_dir.mkdir(parents=True, exist_ok=True)
    api_dir = output_dir / "api"
    api_dir.mkdir(parents=True, exist_ok=True)

    if not args.skip_build:
        _run(["dotnet", "build", "-c", "Release", "src/lunet.slnx"], repo_root)

    projects = _discover_projects(repo_root)
    assemblies: list[Path] = []
    for project in projects:
        assembly = _ensure_assembly_path(repo_root, project)
        if assembly is not None:
            assemblies.append(assembly)

    summary = _run_api_inspector(assemblies, api_dir)
    summary = _apply_source_fallbacks(projects, summary, api_dir)
    summary = _sanitize_generated_paths(repo_root, projects, summary, api_dir)

    # Keep API summary in sync with any fallback updates.
    (api_dir / "summary.json").write_text(
        json.dumps(summary, indent=2) + "\n", encoding="utf-8"
    )

    _write_public_api_index(repo_root, output_dir / "public-api-index.md", summary)
    _write_feature_reference(repo_root, projects, output_dir / "feature-map.md")
    _write_repo_entry_reference(repo_root, output_dir / "build-and-docs-workflow.md")

    # Keep summary for reproducibility.
    (output_dir / "api-summary.json").write_text(
        json.dumps(summary, indent=2) + "\n", encoding="utf-8"
    )

    print(f"[OK] Generated references in: {output_dir}")
    print(f"[OK] API assembly docs: {api_dir}")
    print(f"[OK] API index: {output_dir / 'public-api-index.md'}")
    print(f"[OK] Feature map: {output_dir / 'feature-map.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
