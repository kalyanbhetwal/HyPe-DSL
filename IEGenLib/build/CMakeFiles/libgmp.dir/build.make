# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.15

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/local/apps/cmake/bin/cmake

# The command to remove a file.
RM = /usr/local/apps/cmake/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/KALYANBHETWAL/HyPe-DSL/IEGenLib

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/KALYANBHETWAL/HyPe-DSL/IEGenLib/build

# Utility rule file for libgmp.

# Include the progress variables for this target.
include CMakeFiles/libgmp.dir/progress.make

CMakeFiles/libgmp: CMakeFiles/libgmp-complete


CMakeFiles/libgmp-complete: libgmp-prefix/src/libgmp-stamp/libgmp-install
CMakeFiles/libgmp-complete: libgmp-prefix/src/libgmp-stamp/libgmp-mkdir
CMakeFiles/libgmp-complete: libgmp-prefix/src/libgmp-stamp/libgmp-download
CMakeFiles/libgmp-complete: libgmp-prefix/src/libgmp-stamp/libgmp-update
CMakeFiles/libgmp-complete: libgmp-prefix/src/libgmp-stamp/libgmp-patch
CMakeFiles/libgmp-complete: libgmp-prefix/src/libgmp-stamp/libgmp-configure
CMakeFiles/libgmp-complete: libgmp-prefix/src/libgmp-stamp/libgmp-build
CMakeFiles/libgmp-complete: libgmp-prefix/src/libgmp-stamp/libgmp-install
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/KALYANBHETWAL/HyPe-DSL/IEGenLib/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Completed 'libgmp'"
	/usr/local/apps/cmake/bin/cmake -E make_directory /home/KALYANBHETWAL/HyPe-DSL/IEGenLib/build/CMakeFiles
	/usr/local/apps/cmake/bin/cmake -E touch /home/KALYANBHETWAL/HyPe-DSL/IEGenLib/build/CMakeFiles/libgmp-complete
	/usr/local/apps/cmake/bin/cmake -E touch /home/KALYANBHETWAL/HyPe-DSL/IEGenLib/build/libgmp-prefix/src/libgmp-stamp/libgmp-done

libgmp-prefix/src/libgmp-stamp/libgmp-install: libgmp-prefix/src/libgmp-stamp/libgmp-build
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/KALYANBHETWAL/HyPe-DSL/IEGenLib/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Performing install step for 'libgmp'"
	cd /home/KALYANBHETWAL/HyPe-DSL/IEGenLib/lib/gmp && $(MAKE) install
	cd /home/KALYANBHETWAL/HyPe-DSL/IEGenLib/lib/gmp && /usr/local/apps/cmake/bin/cmake -E touch /home/KALYANBHETWAL/HyPe-DSL/IEGenLib/build/libgmp-prefix/src/libgmp-stamp/libgmp-install

libgmp-prefix/src/libgmp-stamp/libgmp-mkdir:
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/KALYANBHETWAL/HyPe-DSL/IEGenLib/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Creating directories for 'libgmp'"
	/usr/local/apps/cmake/bin/cmake -E make_directory /home/KALYANBHETWAL/HyPe-DSL/IEGenLib/lib/gmp
	/usr/local/apps/cmake/bin/cmake -E make_directory /home/KALYANBHETWAL/HyPe-DSL/IEGenLib/lib/gmp
	/usr/local/apps/cmake/bin/cmake -E make_directory /home/KALYANBHETWAL/HyPe-DSL/IEGenLib/build/libgmp-prefix
	/usr/local/apps/cmake/bin/cmake -E make_directory /home/KALYANBHETWAL/HyPe-DSL/IEGenLib/build/libgmp-prefix/tmp
	/usr/local/apps/cmake/bin/cmake -E make_directory /home/KALYANBHETWAL/HyPe-DSL/IEGenLib/build/libgmp-prefix/src/libgmp-stamp
	/usr/local/apps/cmake/bin/cmake -E make_directory /home/KALYANBHETWAL/HyPe-DSL/IEGenLib/build/libgmp-prefix/src
	/usr/local/apps/cmake/bin/cmake -E make_directory /home/KALYANBHETWAL/HyPe-DSL/IEGenLib/build/libgmp-prefix/src/libgmp-stamp
	/usr/local/apps/cmake/bin/cmake -E touch /home/KALYANBHETWAL/HyPe-DSL/IEGenLib/build/libgmp-prefix/src/libgmp-stamp/libgmp-mkdir

libgmp-prefix/src/libgmp-stamp/libgmp-download: libgmp-prefix/src/libgmp-stamp/libgmp-mkdir
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/KALYANBHETWAL/HyPe-DSL/IEGenLib/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "No download step for 'libgmp'"
	cd /home/KALYANBHETWAL/HyPe-DSL/IEGenLib/build/libgmp-prefix/src && /usr/local/apps/cmake/bin/cmake -E echo_append
	cd /home/KALYANBHETWAL/HyPe-DSL/IEGenLib/build/libgmp-prefix/src && /usr/local/apps/cmake/bin/cmake -E touch /home/KALYANBHETWAL/HyPe-DSL/IEGenLib/build/libgmp-prefix/src/libgmp-stamp/libgmp-download

libgmp-prefix/src/libgmp-stamp/libgmp-update: libgmp-prefix/src/libgmp-stamp/libgmp-download
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/KALYANBHETWAL/HyPe-DSL/IEGenLib/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_5) "No update step for 'libgmp'"
	/usr/local/apps/cmake/bin/cmake -E echo_append
	/usr/local/apps/cmake/bin/cmake -E touch /home/KALYANBHETWAL/HyPe-DSL/IEGenLib/build/libgmp-prefix/src/libgmp-stamp/libgmp-update

libgmp-prefix/src/libgmp-stamp/libgmp-patch: libgmp-prefix/src/libgmp-stamp/libgmp-download
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/KALYANBHETWAL/HyPe-DSL/IEGenLib/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_6) "No patch step for 'libgmp'"
	/usr/local/apps/cmake/bin/cmake -E echo_append
	/usr/local/apps/cmake/bin/cmake -E touch /home/KALYANBHETWAL/HyPe-DSL/IEGenLib/build/libgmp-prefix/src/libgmp-stamp/libgmp-patch

libgmp-prefix/src/libgmp-stamp/libgmp-configure: libgmp-prefix/tmp/libgmp-cfgcmd.txt
libgmp-prefix/src/libgmp-stamp/libgmp-configure: libgmp-prefix/src/libgmp-stamp/libgmp-update
libgmp-prefix/src/libgmp-stamp/libgmp-configure: libgmp-prefix/src/libgmp-stamp/libgmp-patch
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/KALYANBHETWAL/HyPe-DSL/IEGenLib/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_7) "Performing configure step for 'libgmp'"
	cd /home/KALYANBHETWAL/HyPe-DSL/IEGenLib/lib/gmp && autoreconf -f -i
	cd /home/KALYANBHETWAL/HyPe-DSL/IEGenLib/lib/gmp && ./configure --prefix=/home/KALYANBHETWAL/HyPe-DSL/IEGenLib/lib/installed --disable-shared --with-pic
	cd /home/KALYANBHETWAL/HyPe-DSL/IEGenLib/lib/gmp && /usr/local/apps/cmake/bin/cmake -E touch /home/KALYANBHETWAL/HyPe-DSL/IEGenLib/build/libgmp-prefix/src/libgmp-stamp/libgmp-configure

libgmp-prefix/src/libgmp-stamp/libgmp-build: libgmp-prefix/src/libgmp-stamp/libgmp-configure
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/KALYANBHETWAL/HyPe-DSL/IEGenLib/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_8) "Performing build step for 'libgmp'"
	cd /home/KALYANBHETWAL/HyPe-DSL/IEGenLib/lib/gmp && $(MAKE)
	cd /home/KALYANBHETWAL/HyPe-DSL/IEGenLib/lib/gmp && /usr/local/apps/cmake/bin/cmake -E touch /home/KALYANBHETWAL/HyPe-DSL/IEGenLib/build/libgmp-prefix/src/libgmp-stamp/libgmp-build

libgmp: CMakeFiles/libgmp
libgmp: CMakeFiles/libgmp-complete
libgmp: libgmp-prefix/src/libgmp-stamp/libgmp-install
libgmp: libgmp-prefix/src/libgmp-stamp/libgmp-mkdir
libgmp: libgmp-prefix/src/libgmp-stamp/libgmp-download
libgmp: libgmp-prefix/src/libgmp-stamp/libgmp-update
libgmp: libgmp-prefix/src/libgmp-stamp/libgmp-patch
libgmp: libgmp-prefix/src/libgmp-stamp/libgmp-configure
libgmp: libgmp-prefix/src/libgmp-stamp/libgmp-build
libgmp: CMakeFiles/libgmp.dir/build.make

.PHONY : libgmp

# Rule to build all files generated by this target.
CMakeFiles/libgmp.dir/build: libgmp

.PHONY : CMakeFiles/libgmp.dir/build

CMakeFiles/libgmp.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/libgmp.dir/cmake_clean.cmake
.PHONY : CMakeFiles/libgmp.dir/clean

CMakeFiles/libgmp.dir/depend:
	cd /home/KALYANBHETWAL/HyPe-DSL/IEGenLib/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/KALYANBHETWAL/HyPe-DSL/IEGenLib /home/KALYANBHETWAL/HyPe-DSL/IEGenLib /home/KALYANBHETWAL/HyPe-DSL/IEGenLib/build /home/KALYANBHETWAL/HyPe-DSL/IEGenLib/build /home/KALYANBHETWAL/HyPe-DSL/IEGenLib/build/CMakeFiles/libgmp.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/libgmp.dir/depend

