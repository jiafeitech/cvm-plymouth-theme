cvm_ui_desktop_logo_plymouth = configure_file(
  input: 'cvm-ui-desktop-logo.plymouth.in',
  output: '@BASENAME@',
  configuration: {
    'PLYMOUTH_THEME_PATH': plymouth_theme_path,
  },
  install: true,
  install_dir: plymouth_theme_path / 'cvm-ui-desktop-logo',
)

cvm_ui_desktop_logo_scale2_plymouth = configure_file(
  input: 'cvm-ui-desktop-logo-scale-2.plymouth.in',
  output: '@BASENAME@',
  configuration: {
    'PLYMOUTH_THEME_PATH': plymouth_theme_path,
  },
  install: true,
  install_dir: plymouth_theme_path / 'cvm-ui-desktop-logo',
)

install_subdir('logo_assets',
  install_dir:plymouth_theme_path / 'cvm-ui-desktop-logo',
  strip_directory: true,)
