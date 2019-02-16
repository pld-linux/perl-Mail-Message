#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Mail
%define		pnam	Message
%include	/usr/lib/rpm/macros.perl
Summary:	Mail::Message - general message object
Name:		perl-Mail-Message
Version:	3.008
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://cpan.metacpan.org/authors/id/M/MA/MARKOV/Mail-Message-%{version}.tar.gz
# Source0-md5:	cac8626437d21b645e94c4d949f43545
#URL:		https://metacpan.org/release/Mail-Message/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(User::Identity) >= 0.94
BuildRequires:	perl-IO-stringy
BuildRequires:	perl-MIME-Types >= 1.004
BuildRequires:	perl-Mail-Box
BuildRequires:	perl-MailTools >= 2.17
BuildRequires:	perl-TimeDate
BuildRequires:	perl-URI >= 1.23
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Mail::Message object is a container for MIME-encoded message
information, as defined by RFC2822. Everything what is not specificaly
related to storing the messages in mailboxes (folders) is implemented
in this class. Methods which are related to folders is implemented in
the Mail::Box::Message extension.

The main methods are get(), to get information from a message header
field, and decoded() to get the intended content of a message. But
there are many more which can assist your program.

Complex message handling, like construction of replies and forwards,
are implemented in separate packages which are autoloaded into this
class. This means you can simply use these methods as if they are part
of this class. Those package add functionality to all kinds of message
objects.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_vendorlib}/Mail/*.pm
%{perl_vendorlib}/Mail/Box/*
%{perl_vendorlib}/Mail/Message
%{perl_vendorlib}/Mail/*.pod
%{_mandir}/man3/*
