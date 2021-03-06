Summary:	Web-application framework with template engine, control-flow layer, and ORM
Name:		rails
Version:	3.2.9
Release:	2
Source0:	http://rubygems.org/downloads/%{name}-%{version}.gem
License:	MIT
Group:		System/Servers
Url:		http://www.rubyonrails.org/
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

gem install -E -n %{buildroot}%{_bindir} --no-ri --no-rdoc --local --install-dir %{buildroot}/%{ruby_gemdir} --force %{SOURCE0}

rm -rf %{buildroot}%{ruby_gemdir}/cache


%files
%{ruby_gemdir}/gems/%{name}-%{version}
%{ruby_gemdir}/specifications/%{name}-%{version}.gemspec
