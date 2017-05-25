FCN_FILE_DIRS += scripts/startup

scripts_startup_FCN_FILES = \
  scripts/startup/__finish__.m

SITE_STARTUP_FILE_SRC  = scripts/startup/site-rcfile

VERSION_STARTUP_FILE_SRC = scripts/startup/version-rcfile

SYSTEM_INPUTRC_FILE_SRC = scripts/startup/inputrc

STARTUP_FILE_SRC = \
  $(SITE_STARTUP_FILE_SRC) \
  $(VERSION_STARTUP_FILE_SRC) \
  $(SYSTEM_INPUTRC_FILE_SRC)

scripts_startupdir = $(fcnfiledir)/startup

scripts_startup_DATA = $(scripts_startup_FCN_FILES)

FCN_FILES += $(scripts_startup_FCN_FILES)

PKG_ADD_FILES += scripts/startup/PKG_ADD

DIRSTAMP_FILES += scripts/startup/$(octave_dirstamp)

scripts_EXTRA_DIST += $(STARTUP_FILE_SRC)

install-startup-files:
	$(MKDIR_P) $(DESTDIR)$(fcnfiledir)/startup
	if test -f $(DESTDIR)$(fcnfiledir)/startup/octaverc; then true; \
	else \
	  $(INSTALL_DATA) $(srcdir)/$(VERSION_STARTUP_FILE_SRC) \
	    $(DESTDIR)$(fcnfiledir)/startup/octaverc; \
	fi
	if test -f $(DESTDIR)$(fcnfiledir)/startup/inputrc; then true; \
	else \
	  $(INSTALL_DATA) $(srcdir)/$(SYSTEM_INPUTRC_FILE_SRC) \
	    $(DESTDIR)$(fcnfiledir)/startup/inputrc; \
	fi
	$(MKDIR_P) $(DESTDIR)$(localfcnfiledir)/startup
	if test -f $(DESTDIR)$(localfcnfiledir)/startup/octaverc; \
	then true; \
	else \
	  $(INSTALL_DATA) $(srcdir)/$(SITE_STARTUP_FILE_SRC) \
	    $(DESTDIR)$(localfcnfiledir)/startup/octaverc; \
	fi
.PHONY: install-startup-files

uninstall-startup-files:
	rm -f $(DESTDIR)$(fcnfiledir)/startup/octaverc
	rm -f $(DESTDIR)$(fcnfiledir)/startup/inputrc
	rm -f $(DESTDIR)$(localfcnfiledir)/startup/octaverc
.PHONY: uninstall-startup-files
