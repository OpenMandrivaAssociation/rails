Summary:	Web-application framework with template engine, control-flow layer, and ORM
Name:		rails
Version:	2.3.9
Release:	%mkrel 1
Source0:	http://rubygems.org/downloads/%{name}-%{version}.gem
License:	MIT
Group:		System/Servers
Url:		http://www.rubyonrails.org/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
BuildRequires:	ruby-RubyGems

%description
Rails is a full-stack framework for developing database-backed web
applications according to the Model-View-Control pattern. From the
Ajax in the view, to the request and response in the controller, to
the domain model wrapping the database, Rails gives you a pure-Ruby
development environment. To go live, all you need to add is a database
and a web server.

%prep
%setup -c

%build

%install
rm -rf $RPM_BUILD_ROOT

gem install -E -n %{buildroot}%{_bindir} --local --install-dir %{buildroot}/%{ruby_gemdir} --force %{SOURCE0}

rm -rf %{buildroot}%{ruby_gemdir}/cache

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{ruby_gemdir}/gems/%{name}-%{version}
%{ruby_gemdir}/specifications/%{name}-%{version}.gemspec

