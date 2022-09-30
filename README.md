Deep merge

In case the user selects the "Deep merge" option, the system creates a new launch and check items with the following conditions simultaneously:

    test items with the same names
    test items have the same type (SUITE or TEST)
    test items are on the same path (number of parents)
    test items with descendants. If such elements are found only the earliest one is added to the new launch. All descendants are collected on their levels as in the original launches. The merge is started from the upper levels to the lower levels. In case the upper level is not merged, the lower levels will not be merged as well. Items without descendants are not merged despite their level. Status and issues statistics are calculated for a new launch. The original launches are deleted from the system.


https://reportportal.io/docs/Analysis
