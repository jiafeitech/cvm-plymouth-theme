cvm_ui_desktop_bgrt_plymouth = configure_file(
  input: 'cvm-ui-desktop-bgrt.plymouth',
  output: 'cvm-ui-desktop-bgrt.plymouth',
  configuration: {
    'PLYMOUTH_THEME_PATH': plymouth_theme_path,
  },
  install: true,
  install_dir: plymouth_theme_path / 'cvm-ui-desktop-bgrt',
)

install_subdir('bgrt_assets',
  install_dir:plymouth_theme_path / 'cvm-ui-desktop-bgrt',
  strip_directory: true,)
