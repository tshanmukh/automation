Name: vsure-plugininfo-util
Version: 3.0
License: none
Release: 93
AutoReq: 0
Prefix: /centina/sa
Summary: NetOmnia Plugin Information Utility
Group: NetOmnia Utility
Vendor: Centina Systems
Packager: Centina Systems India Pvt Ltd

%description
Netomnia Plugin Information Utility is used to get the latest Plugin Release Notes.

%prep
if [ -e %{home_dir}/rpmbuild/BUILD ]; then
rm -r %{home_dir}/rpmbuild/BUILD
fi
mkdir -p %{home_dir}/rpmbuild/BUILD
if [ -e %{home_dir}/rpmbuild/BUILDROOT ]; then
rm -r %{home_dir}/rpmbuild/BUILDROOT
fi
mkdir %{home_dir}/rpmbuild/BUILDROOT
if [ -e %{home_dir}/rpmbuild/RPMS ]; then
rm -r %{home_dir}/rpmbuild/RPMS
fi
mkdir %{home_dir}/rpmbuild/RPMS
if [ -e %{home_dir}/rpmbuild/SOURCES ]; then
rm -r %{home_dir}/rpmbuild/SOURCES
fi
mkdir %{home_dir}/rpmbuild/SOURCES
if [ -e %{home_dir}/rpmbuild/SRPMS ]; then
rm -r %{home_dir}/rpmbuild/SRPMS
fi
mkdir %{home_dir}/rpmbuild/SRPMS

%build
pwd

%install
mkdir -p %{home_dir}/rpmbuild/BUILDROOT/vsure-plugininfo-util-%{version}-%{release}.x86_64/centina/rpm/%{version}-%{release}/plugininfo-util
mkdir -p %{home_dir}/rpmbuild/BUILDROOT/vsure-plugininfo-util-%{version}-%{release}.x86_64/centina/rpm/%{version}-%{release}/plugininfo-util/pluginPdf
mkdir -p %{home_dir}/rpmbuild/BUILDROOT/vsure-plugininfo-util-%{version}-%{release}.x86_64/centina/rpm/%{version}-%{release}/plugininfo-util/csv
mkdir -p %{home_dir}/rpmbuild/BUILDROOT/vsure-plugininfo-util-%{version}-%{release}.x86_64/centina/rpm/%{version}-%{release}/plugininfo-util/scripts

cd %{repository}
cp -r /home/builduser/repository/centina/sa/profiles/docs/* %{home_dir}/rpmbuild/BUILDROOT/vsure-plugininfo-util-%{version}-%{release}.x86_64/centina/rpm/%{version}-%{release}/plugininfo-util/pluginPdf/
cp /var/www/html/repository/vsureplugin/profile-configs.csv %{home_dir}/rpmbuild/BUILDROOT/vsure-plugininfo-util-%{version}-%{release}.x86_64/centina/rpm/%{version}-%{release}/plugininfo-util/csv/
cp -r %{repository}/../tools/rpmbuild/SPEC/install_scripts/UpdatePluginsInfo.py %{home_dir}/rpmbuild/BUILDROOT/vsure-plugininfo-util-%{version}-%{release}.x86_64/centina/rpm/%{version}-%{release}/plugininfo-util/scripts/

%post
PLUGIN_INFO_UTIL_INSTALL_SCRIPT="/centina/rpm/%{version}-%{release}/plugininfo-util/scripts/UpdatePluginsInfo.py"

echo "About to configure the Latest Plugin Information..."
if [ -f "$PLUGIN_INFO_UTIL_INSTALL_SCRIPT" ]
then
python $PLUGIN_INFO_UTIL_INSTALL_SCRIPT "install" "%{version}-%{release}"
else
echo "ERROR: Plugin Information Update Script not found. Please contact the Administrator."
fi

%files
/centina/rpm/%{version}-%{release}/plugininfo-util

%preun
echo "About to remove the NetOmnia Plugin Information Utility Installation..."
PLUGIN_INFO_UTIL_INSTALL_SCRIPT="/centina/rpm/%{version}-%{release}/plugininfo-util/scripts/UpdatePluginsInfo.py"
if [ -f "$PLUGIN_INFO_UTIL_INSTALL_SCRIPT" ]
then
python $PLUGIN_INFO_UTIL_INSTALL_SCRIPT "uninstall" "%{version}-%{release}"
else
echo "ERROR: Plugin Information Utility uninstall Script not found. Please contact the Administrator."
fi

%postun
rm -rf /centina/rpm/%{version}-%{release}/plugininfo-util


