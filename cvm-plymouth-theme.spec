%define set_theme %{_sbindir}/plymouth-set-default-theme

Name:           cvm-plymouth-theme
Version:        5.1
Release:        1
Summary:        Cvm UI Desktop Plymouth Theme
 
License:        MIT
URL:            https://github.com/jiafeitech/cvm-plymouth-theme
Source0:        https://github.com/jiafeitech/cvm-plymouth-theme/archive/refs/heads/main.tar.gz#/cvm-plymouth-theme-main.tar.gz
BuildArch:      noarch
Requires:       plymouth-plugin-two-step >= 0.7.0
Requires(post): plymouth-scripts

%description
Plymouth Theme for Cvm UI Desktop

%prep
%autosetup -n cvm-plymouth-theme-main

%build

%install
mkdir -p %{buildroot}%{_datadir}/plymouth/themes/cvm-spinner
mkdir -p %{buildroot}%{_datadir}/plymouth/themes/bgrt-cvm
install -m 0644 bgrt-cvm.plymouth %{buildroot}%{_datadir}/plymouth/themes/bgrt-cvm
install -m 0644 cvm-spinner.plymouth *.png *.svg %{buildroot}%{_datadir}/plymouth/themes/cvm-spinner

%post
export LIB=%{_lib}
# on initial install, set this as the new theme
if [ $1 -eq 1 ]; then
    %{set_theme} bgrt-cvm
fi
 
%postun
export LIB=%{_lib}
# if uninstalling, reset to boring meatless default theme
if [ $1 -eq 0 ]; then
    if [ "$(%{set_theme})" == "bgrt-cvm" ]; then
        %{set_theme} --reset
    fi
fi
	
%files
%{_datadir}/plymouth/themes/bgrt-cvm
%{_datadir}/plymouth/themes/cvm-spinner
	
%changelog
* Tue Dec 20 2022 Podter - 5.1-1
- spec file created

