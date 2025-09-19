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
CXXFLAGS 	:= -std=c++11 -O3 -I$(INCLUDE_DIR)

# Source files
MAIN_SRCS 	:= $(SRC_DIR)/main.cpp \
			   $(SRC_DIR)/pset1.cpp

TEST_SRCS 	:= $(SRC_DIR)/test.cpp \
			   $(SRC_DIR)/pset1.cpp

# Target executable
TARGET 		:= $(BUILD_DIR)/matmul

# Default compilation (without OpenBLAS)
$(TARGET): $(MAIN_SRCS)
	$(CXX) $(CXXFLAGS) -o $(TARGET) $(MAIN_SRCS)

# Alternative compilation with OpenBLAS
test: $(TEST_SRCS)
	module load OpenBLAS && $(CXX) $(CXXFLAGS) -o $(BUILD_DIR)/matmul-test $(TEST_SRCS) -lopenblas

###########################
# -------- RULES -------- #
###########################

# Default target
all: clean $(TARGET) test

# Run the target executable
run: $(TARGET)
	$(TARGET)

# Run the test executable
run-test: test
	$(BUILD_DIR)/matmul-test

# Clean up build files
clean:
	rm -f $(TARGET) $(BUILD_DIR)/matmul-test

.PHONY: all run clean test run-test
