Name: 		perl-SOAP-Lite
Version:	0.710.10
Release:	2%{?dist}
Summary:	Client and server side SOAP implementation
License:	GPL+ or Artistic
Group:		Development/Libraries
URL: 		http://search.cpan.org/dist/SOAP-Lite/
Source0: 	http://search.cpan.org/CPAN/authors/id/M/MK/MKUTTER/SOAP-Lite-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:  	perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
BuildRequires:	perl-XML-Parser
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::MockObject)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Task::Weaken)
BuildRequires:  perl(MIME::Parser)
BuildRequires:  perl(Crypt::SSLeay)
BuildRequires:  perl(IO::Socket::SSL)
BuildRequires:  perl(MIME::Lite)
BuildRequires:  perl(Apache)
%if 0%{?fedora}
BuildRequires:  perl(FCGI)
%endif
BuildRequires:  perl(Net::Jabber)
BuildArch: 	noarch

%{?filter_setup:
%filter_from_requires /perl(\(MQ\|Net::\)/d
%filter_from_provides /perl(LWP::Protocol)/d
%?perl_default_filter
}

%description
SOAP::Lite is a collection of Perl modules which provides a simple and
lightweight interface to the Simple Object Access Protocol (SOAP) both on
client and server side.

%prep
%setup -q -n SOAP-Lite-%{version}

%build
%{__perl} Makefile.PL --noprompt INSTALLDIRS=vendor
make %{?_smp_mflags}
find examples -type f |xargs chmod ogu-x

%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%clean
rm -rf $RPM_BUILD_ROOT

%check
make test

%files
%defattr(-,root,root,-)
# For license text(s), see the perl package.
%doc Changes README ReleaseNotes.txt examples
%{_bindir}/*pl
%{perl_vendorlib}/SOAP
%{perl_vendorlib}/Apache
%{perl_vendorlib}/IO
%{perl_vendorlib}/UDDI
%{perl_vendorlib}/XML
%{perl_vendorlib}/XMLRPC
%{_mandir}/man3/*
%{_mandir}/man1/*

%changelog
* Mon Jan 18 2010 Stepan Kasal <skasal@redhat.com> - 0.710.10-2
- limit BR perl(FCGI) to Fedora

* Wed Oct  7 2009 Stepan Kasal <skasal@redhat.com> - 0.710.10-1
- new upstream release
- drop upstreamed patch
- add missing build requires
- use %%filter-* macros

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.710.08-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri May  8 2009 Michael Schwendt <mschwendt@fedoraproject.org> - 0.710.08-3
- Filter out perl(LWP::Protocol) Provides, which comes from a file
  not stored in Perl's search path for modules (#472359).

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.710.08-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Dec 11 2008 Lubomir Rintel <lkundrak@v3.sk> - 0.710.08-1
- New upstream release
- Enable tests
- Include examples in documentation
- Don't grab in dependencies of exotic transports (for the sake
  of consistency with existing practice of Jabber transport)

* Tue Sep 09 2008 Lubomir Rintel <lkundrak@v3.sk> - 0.710.07-2
- Re-add the nil patch

* Tue Jun 24 2008 Mike McGrath <mmcgrath@redhat.com> - 0.710.07-1
- Upstream released new version

* Mon Mar  3 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.68-6
- rebuild for new perl

* Thu Oct 18 2007 Mike McGrath <mmcgrath@redhat.com> - 0.68-5
- Fixed build requires

* Tue Oct 16 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 0.68-4.1
- correct license tag
- add BR: perl(ExtUtils::MakeMaker)

* Mon Mar 03 2007 Mike McGrath <mmcgrath@redhat.com> - 0.68-4
- bogus reqs diff

* Sat Jan 2 2007 Mike McGrath <imlinux@gmail.com> - 0.68-3
- Changed the way this package removes bogus reqs for EL4

* Sun Sep 10 2006 Mike McGrath <imlinux@gmail.com> - 0.68-1
- Rebuild

* Tue Jul 18 2006 Mike McGrath <imlinux@gmail.com> - 0.68-1
- New upstream source
- Patch provided for <value><nil/></value> issues

* Mon Mar 20 2006 Mike McGrath <imlinux@gmail.com> - 0.67-2
- Removed perl requirements that do not yet exist in Extras

* Sat Mar 18 2006 Mike McGrath <imlinux@gmail.com> - 0.67-1
- New Owner and new spec file

* Wed Oct 26 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.60a-3
- Fix build, doc permissions (#169821).

* Wed Apr 06 2005 Hunter Matthews <thm@duke.edu> 0.60a-2
- Review suggestions from José Pedro Oliveira

* Fri Mar 18 2005 Hunter Matthews <thm@duke.edu> 0.60a-1
- Initial packaging.

