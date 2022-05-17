## Requirements, Acceptance Criteria and Test Cases
### General Information
- **Project**: Arabic to Roman Converter
- **Project Description**: Simple app that takes an arabic number, and shows the user its roman equivalent.
- **Author**: Juan Avila 1100378

### Requirements
#### Functional
- **Req1**: The program must be able to take an arabic number and convert it to its roman equivalent
#### Non Functional
##### Performance
The program must take at most 2 seconds between operations. 
##### Compatibility
The program must be able to run on Windows, Linux and MacOS machines with Python 3.7.8 or another compatible version.

### Acceptance Criteria
#### Requirement 1
- **Cri1-1**: The program should not accept empty inputs.
- **Cri1-2**: The program should be able to handle a number between 0 and 3999.
- **Cri1-3**: The program should correctly use the roman notation in the given range (0-3999)

### Test Cases 
#### Unit Tests
##### **UT1-1-1**

| Objective                                  | Input | Expected Result                                     |
|--------------------------------------------|-------|-----------------------------------------------------|
| Check   result after entering empty string |       | Prompt user that the entered input   not an integer |

##### **UT1-2-1**
| Objective                                                    | Input | Expected Result |
|--------------------------------------------------------------|-------|-----------------|
| Check result after entering over the supported range integer | 4000  | MMMM            |
##### **UT1-2-2**
| Objective                                                    | Input | Expected Result |
|--------------------------------------------------------------|-------|-----------------|
| Check result after entering over the supported range integer | 0     | ''              |
##### **UT1-3-1**
| Objective                                                                        | Input | Expected Result |
|----------------------------------------------------------------------------------|-------|-----------------|
| Check if the "repeat a 1 or base 10 letter a max of three times" property is fulfilled | 4     | IV              |
##### **UT1-3-2**
| Objective                                       | Input | Expected Result |
|-------------------------------------------------|-------|-----------------|
| Check if the substraction property is fulfilled | 9     | IX              |
##### **UT1-3-3**
| Objective                                  | Input | Expected Result |
|--------------------------------------------|-------|-----------------|
| Check if the adition property is fulfilled | 12    | IX              |
##### **UT1-3-4**
| Objective                                                               | Input | Expected Result |
|-------------------------------------------------------------------------|-------|-----------------|
| Check if the adition and substraction properties are correctly combined | 19    | XIX             |
##### **UT1-3-5**
| Objective                                                           | Input | Expected Result |
|---------------------------------------------------------------------|-------|-----------------|
| Check if the system correctly applies properties for higher numbers | 2356  | MMCCCLVI        |

#### End to End Tests  
| # | Description                                                                           | Expected Result                                                                    |
|---|---------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| 1 | Run arabictoroman.py from console   (you have to be in the project's root directory). | Command line window should open   and show the program.                            |
| 2 | Give "text" as the   input.                                                           | Message is shown to the user   telling that the given input is not an integer      |
| 3 | Give "Y" as the input                                                                 | Program will reset, telling the   user to write the number that shall be converted |
| 4 | Give "21" as the input                                                                | Console shows XXI to the user                                                      |
| 5 | Give "N" as the input                                                                 | Console shows goodbye message                                                      |
| 6 | Press enter                                                                           | Program closes                                                                     |


