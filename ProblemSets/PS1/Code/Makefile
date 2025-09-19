#!/bin/bash

###########################
# ------ CONSTANTS ------ #
###########################

.DEFAULT_GOAL := all

ROOT_DIR 	:= $(PWD)
SRC_DIR 	:= $(ROOT_DIR)/src
INCLUDE_DIR := $(ROOT_DIR)/include
BUILD_DIR 	:= $(ROOT_DIR)/build

###########################
# ----- COMPILATION ----- #
###########################

# Compilers
CXX 		:= g++

# Compiler flags
CXXFLAGS 	:= -O3 -I$(INCLUDE_DIR)

# Source files
CPP_SRCS 	:= $(SRC_DIR)/main.cpp \
			   $(SRC_DIR)/pset1.cpp \
			   $(SRC_DIR)/test.cpp

# Target executables
TARGET_MM 	:= $(BUILD_DIR)/matmul
TARGET_MM_TEST := $(BUILD_DIR)/matmul-test

# Compile main executable
$(TARGET_MM): $(CPP_SRCS)
	$(CXX) $(CXXFLAGS) -o $(TARGET_MM) $(CPP_SRCS)

# Compile test executable
$(TARGET_MM_TEST):
	module load OpenBLAS && $(CXX) $(CXXFLAGS) -o $(TARGET_MM_TEST) $(CPP_SRCS) -lopenblas

###########################
# -------- RULES -------- #
###########################

# Default target
all: clean $(TARGET)

# Run the target executable
run: $(TARGET)
	$(TARGET)

# Clean up build files
clean:
	rm -f $(TARGET)

.PHONY: all run clean
