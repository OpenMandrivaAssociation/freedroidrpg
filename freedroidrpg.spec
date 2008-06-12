%define name	freedroidrpg
%define	oname	freedroidRPG
%define version	0.10.3
%define release	%mkrel 1
%define	Summary	A Diablo clone with the Tux as hero and the MS as evil power

Summary:	%{Summary}
Name:		%{name}
Version:	%{version}
Release:	%{release}
URL:		http://freedroid.sourceforge.net/
Source0:	%{name}-%{version}.tar.bz2
#Source1:	%{name_lower}-0.9.2.voicesamples.tar.bz2
Source11:	%{name}-16x16.png
Source12:	%{name}-32x32.png
Source13:	%{name}-48x48.png
#Patch:		freedroidRPG-multiline-string.patch.bz2
License:	GPL
Group:		Games/Adventure
BuildRequires:	SDL_image-devel SDL_net-devel SDL_mixer-devel
BuildRequires:	gtk+-devel Mesa-common-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Obsoletes:	%{oname}
Provides:	%{oname} = %{version}-%{release}

%description
The Freedroid RPG is an extension/modification of the classical freedroid
engine into an RPG.  The main differences to the classical version are as
follows:

* The Tux is the main character of the rpg.  He is not displayed as a ball like
  in Freedroid but rather as an animated character, while other droids and
  humans in the game are still represented as the balls with some number or
  code in them.
* Dialogs and chatting with friendly droids and humans:  Multiple-choice menus
  and voice samples (with subtitles for those without sound).
* Melee weapons, armour and other items to be equipped have been added.
* An automap feature was added.
* Saving and loading of games.
* A shop to trade things.
* Controls are different:  Mouse can be used to do everything.  Joystick is not
  supported for moving around any more.
* The archive size (including sound samples) is about 10 times as big as for
  the classical version.  I'd like to appologize to all 56K modem owners at
  this point.

#%package -n	%{name}-voicesamples
#Summary:	Voice samples for Freedroid RPG
#Group:		Games/Adventure
#Requires:	%{name}
#Obsoletes:	%{oname}-voicesamples
#Provides:	%{oname}-voicesamples

#%description -n	%{name}-voicesamples
#This contains optional voice samples used by Freedroid RPG.

%prep
%setup -q
#%patch -p1 -b .strings
rm -rf `find -name .xvpics`

%build
%configure2_5x	--bindir=%{_gamesbindir} \
		--datadir=%{_gamesdatadir}
make clean
%make

%install
rm -rf %{buildroot}
%{makeinstall_std}

# Install voice samples.
#%{__tar} -xjC $RPM_BUILD_ROOT%{_gamesdatadir}/%{name}/sound/speeches -f %{SOURCE1}

install -d %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=FreedroidRPG
Comment=%{Summary}
Exec=%{_gamesbindir}/%{oname}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-MoreApplications-Games-Adventure;Game;AdventureGame;
EOF

install %{SOURCE11} -D %{buildroot}%{_miconsdir}/%{name}.png
install %{SOURCE12} -D %{buildroot}%{_iconsdir}/%{name}.png
install %{SOURCE13} -D %{buildroot}%{_liconsdir}/%{name}.png

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%files -n %{name}
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_datadir}/applications/mandriva*
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%dir %{_gamesdatadir}/%{name}
%dir %{_gamesdatadir}/%{name}/sound
#%dir %{_gamesdatadir}/%{name}/sound/speeches
%{_gamesdatadir}/%{name}/sound/*
%{_gamesdatadir}/%{name}/graphics
%{_gamesdatadir}/%{name}/map
%{_gamesdatadir}/%{name}/sound/effects
%{_gamesdatadir}/%{name}/sound/music
%{_gamesdatadir}/%{name}/dialogs
%{_mandir}/man6/%{oname}.6*
%defattr(755,root,root,755)
%{_gamesbindir}/*

#%files -n %{name}-voicesamples
#%defattr(644,root,root,755)
#%{_gamesdatadir}/%{name}/sound/speeches/*
