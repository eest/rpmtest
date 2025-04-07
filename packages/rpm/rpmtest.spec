Name:       rpmtest
Version:    1
Release:    1
Summary:    Summary for rpmtest
License:    BSD 2-Clause

%description
rpmtest is a test repo for building an rpm out of a go build artifact via github actions

%prep
# we have no source, so nothing here

%build
# the binary is already built, nothing to do here

%install
mkdir -p %{buildroot}/usr/bin/
install -m 755 rpmtest %{buildroot}/usr/bin/rpmtest

%files
/usr/bin/rpmtest

%changelog
# let's skip this for now
