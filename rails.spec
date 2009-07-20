%define name	rails
%define version 2.3.3
%define release %mkrel 1

Summary:	Web-application framework with template engine, control-flow layer, and ORM
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{version}.gem
License:	MIT
Group:		System/Servers
Url:		http://www.rubyonrails.org/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
BuildRequires:	ruby-RubyGems
Requires:	ruby-RubyGems
Requires:	ruby-activesupport = %{version}
Requires:	ruby-activerecord = %{version}
Requires:	ruby-actionpack = %{version}
Requires:	ruby-actionmailer = %{version}
Requires:	ruby-actionwebservice
Requires:	ruby-activeresource = %{version}
Requires:	ruby-sqlite3
Requires:	ruby-rake >= 0.8.1

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

# (the poor buildroot way)
# perl -pe "s,^\s+DESTDIR\s+=.*,  DESTDIR = '$RPM_BUILD_ROOT'," %{ruby_archdir}/rbconfig.rb > rbconfig.rb
# ruby -I . /usr/bin/gem install --ignore-dependencies %{SOURCE0}

install -d $RPM_BUILD_ROOT%{ruby_gemdir}
gem install --ignore-dependencies --install-dir $RPM_BUILD_ROOT%{ruby_gemdir} %{SOURCE0}
install -d $RPM_BUILD_ROOT%{_bindir}
mv $RPM_BUILD_ROOT%{ruby_gemdir}/bin/* $RPM_BUILD_ROOT%{_bindir}
rm -rf $RPM_BUILD_ROOT%{ruby_gemdir}/bin
rm -rf  $RPM_BUILD_ROOT%{ruby_gemdir}/doc/%{name}-%{version}
rm -rf $RPM_BUILD_ROOT%{ruby_gemdir}/doc

for f in `find $RPM_BUILD_ROOT%{ruby_gemdir}/gems/%{name}-%{version} -type f`
do
        if head -n1 "$f" | grep '^#!' >/dev/null;
        then
                sed -i 's|/usr/local/bin|/usr/bin|' "$f"
                chmod 0755 "$f"
        else
                chmod 0644 "$f"
        fi
done


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{ruby_gemdir}/gems/%{name}-%{version}
%{ruby_gemdir}/cache/%{name}-%{version}.gem
%{ruby_gemdir}/specifications/%{name}-%{version}.gemspec

