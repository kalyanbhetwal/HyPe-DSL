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

# Include any dependencies generated for this target.
include tutorial/CMakeFiles/mttkrp.dir/depend.make

# Include the progress variables for this target.
include tutorial/CMakeFiles/mttkrp.dir/progress.make

# Include the compile flags for this target's objects.
include tutorial/CMakeFiles/mttkrp.dir/flags.make

tutorial/CMakeFiles/mttkrp.dir/mttkrp.cc.o: tutorial/CMakeFiles/mttkrp.dir/flags.make
tutorial/CMakeFiles/mttkrp.dir/mttkrp.cc.o: ../tutorial/mttkrp.cc
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/KALYANBHETWAL/HyPe-DSL/IEGenLib/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object tutorial/CMakeFiles/mttkrp.dir/mttkrp.cc.o"
	cd /home/KALYANBHETWAL/HyPe-DSL/IEGenLib/build/tutorial && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/mttkrp.dir/mttkrp.cc.o -c /home/KALYANBHETWAL/HyPe-DSL/IEGenLib/tutorial/mttkrp.cc

tutorial/CMakeFiles/mttkrp.dir/mttkrp.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/mttkrp.dir/mttkrp.cc.i"
	cd /home/KALYANBHETWAL/HyPe-DSL/IEGenLib/build/tutorial && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/KALYANBHETWAL/HyPe-DSL/IEGenLib/tutorial/mttkrp.cc > CMakeFiles/mttkrp.dir/mttkrp.cc.i

tutorial/CMakeFiles/mttkrp.dir/mttkrp.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/mttkrp.dir/mttkrp.cc.s"
	cd /home/KALYANBHETWAL/HyPe-DSL/IEGenLib/build/tutorial && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/KALYANBHETWAL/HyPe-DSL/IEGenLib/tutorial/mttkrp.cc -o CMakeFiles/mttkrp.dir/mttkrp.cc.s

# Object files for target mttkrp
mttkrp_OBJECTS = \
"CMakeFiles/mttkrp.dir/mttkrp.cc.o"

# External object files for target mttkrp
mttkrp_EXTERNAL_OBJECTS =

bin/tutorial/mttkrp: tutorial/CMakeFiles/mttkrp.dir/mttkrp.cc.o
bin/tutorial/mttkrp: tutorial/CMakeFiles/mttkrp.dir/build.make
bin/tutorial/mttkrp: src/libiegenlib.a
bin/tutorial/mttkrp: tutorial/CMakeFiles/mttkrp.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/KALYANBHETWAL/HyPe-DSL/IEGenLib/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable ../bin/tutorial/mttkrp"
	cd /home/KALYANBHETWAL/HyPe-DSL/IEGenLib/build/tutorial && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/mttkrp.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
tutorial/CMakeFiles/mttkrp.dir/build: bin/tutorial/mttkrp

.PHONY : tutorial/CMakeFiles/mttkrp.dir/build

tutorial/CMakeFiles/mttkrp.dir/clean:
	cd /home/KALYANBHETWAL/HyPe-DSL/IEGenLib/build/tutorial && $(CMAKE_COMMAND) -P CMakeFiles/mttkrp.dir/cmake_clean.cmake
.PHONY : tutorial/CMakeFiles/mttkrp.dir/clean

tutorial/CMakeFiles/mttkrp.dir/depend:
	cd /home/KALYANBHETWAL/HyPe-DSL/IEGenLib/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/KALYANBHETWAL/HyPe-DSL/IEGenLib /home/KALYANBHETWAL/HyPe-DSL/IEGenLib/tutorial /home/KALYANBHETWAL/HyPe-DSL/IEGenLib/build /home/KALYANBHETWAL/HyPe-DSL/IEGenLib/build/tutorial /home/KALYANBHETWAL/HyPe-DSL/IEGenLib/build/tutorial/CMakeFiles/mttkrp.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : tutorial/CMakeFiles/mttkrp.dir/depend
