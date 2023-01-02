cvm_ui_desktop_bgrt_plymouth = i18n.merge_file(
  input: configure_file(
    input: 'cvm-ui-desktop-bgrt.plymouth.desktop',
    output: 'cvm-ui-desktop-bgrt.plymouth.desktop',
    configuration: {
      'PLYMOUTH_THEME_PATH': plymouth_theme_path,
    },
  ),
  output: 'cvm-ui-desktop-bgrt.plymouth',
  type: 'desktop',
  po_dir: po_dir,
  install: true,
  install_dir: plymouth_theme_path / 'cvm-ui-desktop-bgrt',
)

install_subdir('bgrt_assets',
  install_dir:plymouth_theme_path / 'cvm-ui-desktop-bgrt',
  strip_directory: true,)
