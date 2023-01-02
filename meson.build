project('plymouth-theme-cvm-ui-desktop',
  meson_version: '>= 0.61',
  version: '0.0.8',
  license : 'MIT',
  default_options: ['prefix=/usr']
)

# Path variables
plymouth_theme_path = get_option('prefix') / get_option('datadir') / 'plymouth' / 'themes'

# config
conf = configuration_data()
conf.set_quoted('PLYMOUTH_THEME_PATH', plymouth_theme_path)

# Subdirectories
subdir('src')
