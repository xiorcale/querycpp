CXX = clang++
CXX_FLAGS = -std=c++17 -c
LINK_FLAGS = -lfmt

INCLUDE_FLAGS = -I./include

SRC_DIR = src/

all: database_data_type_build column_build table_build query_build


query_build:
	$(CXX) $(CXX_FLAGS) $(INCLUDE_FLAGS) $(SRC_DIR)query.cpp $(LINK_FLAGS)

table_build:
	$(CXX) $(CXX_FLAGS) $(INCLUDE_FLAGS) $(SRC_DIR)table.cpp

column_build:
	$(CXX) $(CXX_FLAGS) $(INCLUDE_FLAGS) $(SRC_DIR)column.cpp

database_data_type_build:
	$(CXX) $(CXX_FLAGS) $(INCLUDE_FLAGS) $(SRC_DIR)database_data_type.cpp


clean:

	rm *.o
