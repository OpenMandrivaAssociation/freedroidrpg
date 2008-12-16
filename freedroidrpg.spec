%define name	freedroidrpg
%define	oname	freedroidRPG
%define version	0.11.1
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
FreeDroidRPG is a free isometric RPG game inspired by elements of Diablo and
Fallout. Originally based on FreeDroid Classic, this project now has vastly deviated
from its parent.

This game tells the story of a world destroyed by a conflict between the bots
and their human masters. Play as Tux in a quest to save the world from the murderous
rebel bots who know no mercy. You get to choose which path you wish to follow, and
freedom of choice is everywhere in the game.

FreeDroidRPG features a complete real time combat system with melee and ranged
weapons, fairly similar to the proprietary game Diablo. There also is an 
innovative system of magic, with features such as forced casting and over 20 spells.
You can use over 50 different kinds of items and fight countless enemies on
your way to your destiny.

We have an advanced dialogue system, which aims at being at least on par with
Fallout's. The dialogues in the game represent a large part of the gameplay.
Finally, if guns are too inaccurate and blades too messy, you can always take
over your enemies and have them fight on your side."



%prep
%setup -q
rm -rf `find -name .xvpics`

%build
%configure2_5x	--bindir=%{_gamesbindir} \
		--datadir=%{_gamesdatadir}
make clean
%make

%install
rm -rf %{buildroot}
%{makeinstall_std}

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
Categories=Game;AdventureGame;
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
%{_gamesdatadir}/%{name}/sound/*
%{_gamesdatadir}/%{name}/graphics
%{_gamesdatadir}/%{name}/map
%{_gamesdatadir}/%{name}/dialogs
%{_gamesdatadir}/%{name}/locale
%{_mandir}/man6/%{oname}.6*
%defattr(755,root,root,755)
%{_gamesbindir}/*
