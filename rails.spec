Summary:	Web-application framework with template engine, control-flow layer, and ORM
Name:		rails
Version:	7.0.4.3
Release:	1
Source0:	http://rubygems.org/downloads/%{name}-%{version}.gem
License:	MIT
Group:		System/Servers
Url:		https://www.rubyonrails.org/
BuildArch:	noarch
BuildRequires:	ruby

%description
Rails is a full-stack framework for developing database-backed web
applications according to the Model-View-Control pattern. From the
Ajax in the view, to the request and response in the controller, to
the domain model wrapping the database, Rails gives you a pure-Ruby
development environment. To go live, all you need to add is a database
and a web server.

%prep
%autosetup -p1 -c

%build

%install

gem install -E -n %{buildroot}%{_bindir} --local --install-dir %{buildroot}/%{ruby_gemdir} --force %{SOURCE0}

rm -rf %{buildroot}%{ruby_gemdir}/cache


%files
%{ruby_gemdir}/gems/%{name}-%{version}
%{ruby_gemdir}/specifications/%{name}-%{version}.gemspec
%doc %{ruby_gemdir}/doc/%{name}-%{version}
