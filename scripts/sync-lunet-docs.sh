#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
OUT_DIR="${1:-${SKILL_DIR}/references/upstream}"
LUNET_DIR="${OUT_DIR}/lunet-docs"
TEMPLATES_DIR="${OUT_DIR}/templates"
REPOS_DIR="${OUT_DIR}/repos"
LUNET_REPO_DIR="${REPOS_DIR}/lunet"
TEMPLATES_REPO_DIR="${REPOS_DIR}/templates"
SOURCE_MAP="${SKILL_DIR}/references/00-prefetch-source-map.md"

mkdir -p "${LUNET_DIR}/plugins" "${TEMPLATES_DIR}/dist" "${REPOS_DIR}"

LUNET_FILES=(
  "readme.md"
  "getting-started.md"
  "cli.md"
  "configuration.md"
  "content-and-frontmatter.md"
  "site-structure.md"
  "layouts-and-includes.md"
  "themes-and-extends.md"
  "github-actions.md"
  "menu.yml"
  "plugins/readme.md"
  "plugins/api-dotnet.md"
  "plugins/api.md"
  "plugins/attributes.md"
  "plugins/bundles.md"
  "plugins/cards.md"
  "plugins/data.md"
  "plugins/datas.md"
  "plugins/extends.md"
  "plugins/json.md"
  "plugins/markdown.md"
  "plugins/menus.md"
  "plugins/menu.yml"
  "plugins/minifier.md"
  "plugins/resources.md"
  "plugins/rss.md"
  "plugins/scss.md"
  "plugins/search.md"
  "plugins/server.md"
  "plugins/sitemaps.md"
  "plugins/summarizer.md"
  "plugins/taxonomies.md"
  "plugins/toml.md"
  "plugins/tracking.md"
  "plugins/watcher.md"
  "plugins/yaml.md"
)

TEMPLATES_FILES=(
  "readme.md"
  "dist/readme.md"
  "dist/config.scriban"
  "dist/menu.yml"
)

sync_repo() {
  local repo_url="$1"
  local repo_dir="$2"
  shift 2
  local sparse_paths=("$@")

  git clone --depth 1 --filter=blob:none --sparse "${repo_url}" "${repo_dir}"
  git -C "${repo_dir}" sparse-checkout set "${sparse_paths[@]}"
}

resolve_branch() {
  local repo_dir="$1"
  local branch

  branch="$(git -C "${repo_dir}" symbolic-ref --quiet --short refs/remotes/origin/HEAD 2>/dev/null | sed 's#^origin/##' || true)"
  if [[ -n "${branch}" ]]; then
    echo "${branch}"
    return
  fi

  if git -C "${repo_dir}" show-ref --verify --quiet refs/remotes/origin/main; then
    echo "main"
    return
  fi

  if git -C "${repo_dir}" show-ref --verify --quiet refs/remotes/origin/master; then
    echo "master"
    return
  fi

  branch="$(git -C "${repo_dir}" symbolic-ref --quiet --short HEAD || true)"
  if [[ -n "${branch}" ]]; then
    echo "${branch}"
    return
  fi

  echo "main"
}

update_repo() {
  local repo_url="$1"
  local repo_dir="$2"
  shift 2
  local sparse_paths=("$@")
  local branch

  git -C "${repo_dir}" remote set-url origin "${repo_url}"
  git -C "${repo_dir}" fetch --depth 1 origin
  git -C "${repo_dir}" sparse-checkout set "${sparse_paths[@]}"

  branch="$(resolve_branch "${repo_dir}")"
  if git -C "${repo_dir}" show-ref --verify --quiet "refs/remotes/origin/${branch}"; then
    git -C "${repo_dir}" checkout -B "${branch}" "origin/${branch}"
  else
    echo "[warn] Remote branch origin/${branch} not found in ${repo_dir}; keeping current checkout." >&2
  fi
}

official_url_for_lunet_file() {
  local file="$1"
  if [[ "${file}" == "readme.md" ]]; then
    echo "https://lunet.io/docs/"
    return
  fi
  if [[ "${file}" == "plugins/readme.md" ]]; then
    echo "https://lunet.io/docs/plugins/"
    return
  fi
  if [[ "${file}" == *.md && "${file}" == plugins/* ]]; then
    local name="${file##*/}"
    name="${name%.md}"
    echo "https://lunet.io/docs/plugins/${name}/"
    return
  fi
  if [[ "${file}" == *.md ]]; then
    local name="${file%.md}"
    echo "https://lunet.io/docs/${name}/"
    return
  fi
  echo "N/A (docs source only)"
}

official_url_for_template_file() {
  local file="$1"
  echo "https://github.com/lunet-io/templates/blob/main/${file}"
}

echo "Syncing Lunet docs repos into: ${REPOS_DIR}"

if [[ -d "${LUNET_REPO_DIR}/.git" ]]; then
  update_repo "https://github.com/lunet-io/lunet.git" "${LUNET_REPO_DIR}" \
    "site/docs" \
    "readme.md"
else
  sync_repo "https://github.com/lunet-io/lunet.git" "${LUNET_REPO_DIR}" \
    "site/docs" \
    "readme.md"
fi

if [[ -d "${TEMPLATES_REPO_DIR}/.git" ]]; then
  update_repo "https://github.com/lunet-io/templates.git" "${TEMPLATES_REPO_DIR}" \
    "readme.md" \
    "dist"
else
  sync_repo "https://github.com/lunet-io/templates.git" "${TEMPLATES_REPO_DIR}" \
    "readme.md" \
    "dist"
fi

LUNET_COMMIT="$(git -C "${LUNET_REPO_DIR}" rev-parse HEAD)"
TEMPLATES_COMMIT="$(git -C "${TEMPLATES_REPO_DIR}" rev-parse HEAD)"

echo "Lunet repo commit: ${LUNET_COMMIT}"
echo "Templates repo commit: ${TEMPLATES_COMMIT}"
echo "Materializing docs snapshots into: ${OUT_DIR}"

for file in "${LUNET_FILES[@]}"; do
  src="${LUNET_REPO_DIR}/site/docs/${file}"
  dest="${LUNET_DIR}/${file}"
  mkdir -p "$(dirname "${dest}")"
  cp "${src}" "${dest}"
  echo "  lunet: ${file}"
done

for file in "${TEMPLATES_FILES[@]}"; do
  src="${TEMPLATES_REPO_DIR}/${file}"
  dest="${TEMPLATES_DIR}/${file}"
  mkdir -p "$(dirname "${dest}")"
  cp "${src}" "${dest}"
  echo "  templates: ${file}"
done

manifest_tmp="$(mktemp)"
{
  echo "_Last synced (UTC): $(date -u +"%Y-%m-%dT%H:%M:%SZ")_"
  echo
  echo "- Lunet repo commit: \`${LUNET_COMMIT}\`"
  echo "- Templates repo commit: \`${TEMPLATES_COMMIT}\`"
  echo
  echo "| Category | Canonical URL | Source URL | Local path |"
  echo "|---|---|---|---|"
  for file in "${LUNET_FILES[@]}"; do
    canonical="$(official_url_for_lunet_file "${file}")"
    src="https://github.com/lunet-io/lunet/blob/${LUNET_COMMIT}/site/docs/${file}"
    local_path="references/upstream/lunet-docs/${file}"
    echo "| Lunet docs | ${canonical} | ${src} | ${local_path} |"
  done
  for file in "${TEMPLATES_FILES[@]}"; do
    canonical="$(official_url_for_template_file "${file}")"
    src="https://github.com/lunet-io/templates/blob/${TEMPLATES_COMMIT}/${file}"
    local_path="references/upstream/templates/${file}"
    echo "| Templates | ${canonical} | ${src} | ${local_path} |"
  done
} > "${manifest_tmp}"

if [[ -f "${SOURCE_MAP}" ]]; then
  updated_tmp="$(mktemp)"
  awk -v begin="<!-- BEGIN GENERATED: DOC SYNC MANIFEST -->" \
      -v end="<!-- END GENERATED: DOC SYNC MANIFEST -->" \
      -v manifest_file="${manifest_tmp}" '
      $0 == begin {
        print
        while ((getline line < manifest_file) > 0) {
          print line
        }
        in_block = 1
        next
      }
      $0 == end {
        in_block = 0
        print
        next
      }
      !in_block { print }
  ' "${SOURCE_MAP}" > "${updated_tmp}"
  mv "${updated_tmp}" "${SOURCE_MAP}"
  echo "Updated manifest in: ${SOURCE_MAP}"
fi

echo "Sync complete."
