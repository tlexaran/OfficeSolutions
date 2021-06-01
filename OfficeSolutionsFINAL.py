import sqlite3
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

conn = sqlite3.connect("OS_Employee.db")
xl = pd.ExcelFile("SalesData.xlsx")
OrderData = xl.parse("Orders")

def customer_loyalty():
    print("\n1. Top Customers by Frequency\n2. Top Customers by Recency\n3. Top Customers by Quantity\n4. Return to Main Menu")
    loyalty_menu = input("Please enter a digit that is 1 - 4: ").strip()
    
    # Checks if user entered a digit
    while not loyalty_menu.isdigit():
        loyalty_menu = input("Please enter a digit that is 1 - 4: ").strip()
    
    # Checks if user entered a digit that is from 1-4
    while int(loyalty_menu) < 0 and int(loyalty_menu) > 4:
        loyalty_menu = input("Please enter any option from 1 - 4: ").strip()
        
    if loyalty_menu == '1':
        print("\nTop Customers by Frequency")
        display_data = input("Enter the amount of products you would like to be displayed (MAX: 15): ").strip()
        
        while not display_data.isdigit():
            display_data = input("Display product amount has to be a digit. Please try again: ").strip()
        
        while int(display_data) <= 0 or int(display_data) > 15:
            if int(display_data) <= 0:
                display_data = input("Display product amount cannot be less than/equal to 0. Please try again: ").strip()
            
            if int(display_data) > 15:
                display_data = input("Display product amount exceeded maximum of 15. Please try again: ").strip()
                
        print("\nTop " + display_data + " Customers by Frequency\n")
        
        MostFrequent = OrderData["Customer Name"].value_counts() # this is the line that  determines each customer's number of orders.
        MostFrequent = MostFrequent.reset_index()
        print(MostFrequent.head(int(display_data)))
        
        print("\nCompared to Top " + display_data + " Most Profitable Customers\n")
        MostFrequentProfit = OrderData[["Customer Name", "Profit"]]
        SortProfit = MostFrequentProfit.sort_values(by = "Profit", ascending = False)
        print(SortProfit.head(int(display_data)))
        
        print("\n1. Back to Customer Loyalty Menu\n2. Back to Main Menu\n3. Log Out\n")
        customer_sub_menu = input("Please any option from 1 - 3: ").strip()
        
        # Checks if user entered a digit
        while not customer_sub_menu.isdigit():
            customer_sub_menu = input("Please enter a digit that is 1 - 3: ").strip()
    
        # Checks if user entered a digit that is from 1-4
        while int(customer_sub_menu) < 0 or int(customer_sub_menu) > 3:
            customer_sub_menu = input("Please enter any option from 1 - 3: ").strip()
        
        if customer_sub_menu == '1':
            customer_loyalty()
        elif customer_sub_menu == '2':
            main_menu()
        else:
            login()
            
    elif loyalty_menu == '2':
        print("\nTop Customers by Recency\n")
        
        display_data = input("How many customers would you like displayed? (MAX: 15): ").strip()
        
        while not display_data.isdigit():
            display_data = input("Display customer amount has to be a digit. Please try again: ").strip()
        
        while int(display_data) <= 0 or int(display_data) > 15:
            if int(display_data) <= 0:
                display_data = input("Display customer amount cannot be less than/equal to 0. Please try again: ").strip()
            
            if int(display_data) > 15:
                display_data = input("Display customer amount exceeded maximum of 15. Please try again: ").strip()
                
        print("\nTop " + display_data + " Customers by Recency\n")
        
        Customer_OrderDate = OrderData[["Order Date", "Customer Name", "Profit"]]
        SortDates = Customer_OrderDate.sort_values(by = "Order Date", ascending = False)
        SortDate_noDup = SortDates.drop_duplicates(subset= "Customer Name" , keep = "first")
        print(SortDate_noDup.head(int(display_data)))
        
        print("\n1. Back to Customer Loyalty Menu\n2. Back to Main Menu\n3. Log Out\n")
        customer_sub_menu = input("Please any option from 1 - 3: ").strip()
        
        # Checks if user entered a digit
        while not customer_sub_menu.isdigit():
            customer_sub_menu = input("Please enter a digit that is 1 - 3: ").strip()
    
        # Checks if user entered a digit that is from 1-4
        while int(customer_sub_menu) < 0 or int(customer_sub_menu) > 3:
            customer_sub_menu = input("Please enter any option from 1 - 3: ").strip()
        
        if customer_sub_menu == '1':
            customer_loyalty()
        elif customer_sub_menu == '2':
            main_menu()
        else:
            login()
                
    elif loyalty_menu == '3':
        print("\nTop Customers by Quantity\n")
        display_data = input("How many customers would you like displayed? (MAX: 15): ").strip()
        
        while not display_data.isdigit():
            display_data = input("Display customer amount has to be a digit. Please try again: ").strip()
        
        while int(display_data) <= 0 or int(display_data) > 15:
            if int(display_data) <= 0:
                display_data = int(input("Display customer amount cannot be less than/equal to 0. Please try again: ")).strip()
            
            if int(display_data) > 15:
                display_data = input("Display customer amount exceeded maximum of 15. Please try again: ").strip()
                
        print("\nTop " + display_data + " of Customers by Quantity")
        
        Customer_OrderDate = OrderData[["Customer Name", "Quantity", "Profit"]]
        SortDates = Customer_OrderDate.sort_values(by = "Quantity", ascending = False)
        SortDate_noDup = SortDates.drop_duplicates(subset= "Customer Name" , keep = "first")
        print(SortDate_noDup.head(int(display_data)))
        
        print("\n1. Back to Customer Loyalty Menu\n2. Back to Main Menu\n3. Log Out\n")
        customer_sub_menu = input("Please any option from 1 - 3: ").strip()
        
        # Checks if user entered a digit
        while not customer_sub_menu.isdigit():
            customer_sub_menu = input("Please enter a digit that is 1 - 3: ").strip()
    
        # Checks if user entered a digit that is from 1-4
        while int(customer_sub_menu) < 0 or int(customer_sub_menu) > 3:
            customer_sub_menu = input("Please enter any option from 1 - 3: ").strip()
        
        if customer_sub_menu == '1':
            customer_loyalty()
        elif customer_sub_menu == '2':
            main_menu()
        else:
            login()
    else:
        main_menu()

def art():
    print("\n1. Comparison To Other Products\n2. Trend Analysis\n3. Customer Trends Analysis\n4. Return to Main Menu\n")
    highend_art_menu = input("Please choose from 1 - 4: ")
    
    # Checks if user entered a digit
    while not highend_art_menu.isdigit():
        highend_art_menu = input("Please enter a digit that is 1 - 4: ").strip()
    
    # Checks if user entered a digit that is from 1-4
    while int(highend_art_menu) < 0 or int(highend_art_menu) > 4:
        highend_art_menu = input("Please enter any option from 1 - 4: ").strip()
    
    if highend_art_menu == '1':
        print("\nComparison To Other Products\n")
        
        print("The most profitable Sub-Category of products: ")
        Product_Profit = OrderData[["Sub-Category", "Profit"]]
        Product_Total_Profit = Product_Profit.groupby(by= "Sub-Category").sum().sort_values(by = "Profit" , ascending = False)
        print(Product_Total_Profit.head(30))
        Decorating = "\n" + "~"*45 + "\n"
        print(Decorating) 
        
        print("\n1. Back to Art Menu\n2. Back to Main Menu\n3. Log Out\n")
        art_sub_menu = input("Please any option from 1 - 3: ").strip()
        
        # Checks if user entered a digit
        while not art_sub_menu.isdigit():
            art_sub_menu = input("Please enter a digit that is 1 - 3: ").strip()
    
        # Checks if user entered a digit that is from 1-4
        while int(art_sub_menu) < 0 or int(art_sub_menu) > 3:
            art_sub_menu = input("Please enter any option from 1 - 3: ").strip()
        
        if art_sub_menu == '1':
            art()
        elif art_sub_menu == '2':
            main_menu()
        else:
            login()
        
    elif highend_art_menu == '2':
        print("\nTrend Analysis Menu\n")
        print("Would you like to see a:\n1. Monthly Analysis\n2. Yearly Analysis\n3. Back To Art Menu")
        
        TA_menu = input("Please choose any option from 1 - 2: ")
        
        if TA_menu == '1':
            print("\nMonthly Analysis\n")
        
            MonthlySales = OrderData
            MonthlySales["Month"] = MonthlySales["Order Date"].dt.month
            Sales = MonthlySales[["Profit", "Month", "Sub-Category"]]
            Art_SubCategory = Sales.loc[Sales["Sub-Category"] == "Art"]
            TotalSales = Art_SubCategory.groupby(by="Month").sum().sort_values(by = "Month", ascending = True )
            TotalSales = TotalSales.reset_index()
            print(TotalSales)
            
            sns.set(rc={'figure.figsize':(10,9)})
            barchart1 = sns.barplot(x="Month", y = "Profit", data = TotalSales)
            barchart1.set_title("Art Profit by Month")
            plt.show()
            
            print("\n1. Back to Trend Analysis Menu\n2. Back to Art Menu\n3. Back to Main Menu\n4. Log Out\n")
            art_sub_menu = input("Please any option from 1 - 4: ").strip()
        
        elif TA_menu == '2':
            print("\nYearly Analysis\n")
        
            MonthlySales = OrderData
            MonthlySales["Year"] = MonthlySales["Order Date"].dt.year
            Sales = MonthlySales[["Profit", "Year", "Sub-Category"]]
            Art_SubCategory = Sales.loc[Sales["Sub-Category"] == "Art"]
            TotalSales = Art_SubCategory.groupby(by="Year").sum().sort_values(by = "Year", ascending = False )
            TotalSales = TotalSales.reset_index()
            print(TotalSales)
            
            sns.set(rc={'figure.figsize':(10,9)})
            barchart1 = sns.barplot(x="Year", y = "Profit", data = TotalSales)
            barchart1.set_title("Art Profit by Year")
            plt.show()
            
            print("\n1. Back to Trend Analysis Menu\n2. Back to Art Menu\n3. Back to Main Menu\n4. Log Out\n")
            art_sub_menu = input("Please any option from 1 - 4: ").strip()
        else:
            art()

        
        # Checks if user entered a digit
        while not art_sub_menu.isdigit():
            art_sub_menu = input("Please enter a digit that is 1 - 4: ").strip()
    
        # Checks if user entered a digit that is from 1-4
        while int(art_sub_menu) < 0 or int(art_sub_menu) > 4:
            art_sub_menu = input("Please enter any option from 1 - 4: ").strip()
        
        while art_sub_menu == '1':
            print("\nTrend Analysis Menu\n")
            print("Would you like to see a:\n1. Monthly Analysis\n2. Yearly Analysis\n3. Back To Art Menu")
            
            TA_menu = input("Please choose any option from 1 - 2: ")
            
            if TA_menu == '1':
                print("\nMonthly Analysis\n")
            
                MonthlySales = OrderData
                MonthlySales["Month"] = MonthlySales["Order Date"].dt.month
                Sales = MonthlySales[["Profit", "Month", "Sub-Category"]]
                Art_SubCategory = Sales.loc[Sales["Sub-Category"] == "Art"]
                TotalSales = Art_SubCategory.groupby(by="Month").sum().sort_values(by = "Month", ascending = True )
                TotalSales = TotalSales.reset_index()
                print(TotalSales)
                
                sns.set(rc={'figure.figsize':(10,9)})
                barchart1 = sns.barplot(x="Month", y = "Profit", data = TotalSales)
                barchart1.set_title("Art Profit by Month")
                plt.show()
                
                print("\n1. Back to Trend Analysis Menu\n2. Back to Art Menu\n3. Back to Main Menu\n4. Log Out\n")
                art_sub_menu = input("Please any option from 1 - 4: ").strip()
            
            elif TA_menu == '2':
                print("\nYearly Analysis\n")
            
                MonthlySales = OrderData
                MonthlySales["Year"] = MonthlySales["Order Date"].dt.year
                Sales = MonthlySales[["Profit", "Year", "Sub-Category"]]
                Art_SubCategory = Sales.loc[Sales["Sub-Category"] == "Art"]
                TotalSales = Art_SubCategory.groupby(by="Year").sum().sort_values(by = "Year", ascending = False )
                TotalSales = TotalSales.reset_index()
                print(TotalSales)
                
                sns.set(rc={'figure.figsize':(10,9)})
                barchart1 = sns.barplot(x="Year", y = "Profit", data = TotalSales)
                barchart1.set_title("Art Profit by Year")
                plt.show()
                
                print("\n1. Back to Trend Analysis Menu\n2. Back to Art Menu\n3. Back to Main Menu\n4. Log Out\n")
                art_sub_menu = input("Please any option from 1 - 4: ").strip()
            else:
                art()

        if art_sub_menu == '2':
            art()
        elif art_sub_menu == '3':
            main_menu()
        else:
            login()
        
    elif highend_art_menu == '3':
        print("\nCustomer Trend Analysis\n")
        
        Product_Profit = OrderData[["Segment", "Sub-Category", "Sales"]]
        Art_SubCategory = Product_Profit.loc[Product_Profit["Sub-Category"] == "Art"]
        Product_Total_Profit = Art_SubCategory.groupby(by = ["Segment", "Sub-Category"]).sum().sort_values(by = "Sales", ascending = False )
        print(Product_Total_Profit.head(5))
        
        print("\n1. Back to Art Menu\n2. Back to Main Menu\n3. Log Out\n")
        art_sub_menu = input("Please enter any option from 1 - 3: ").strip()
        
        # Checks if user entered a digit
        while not art_sub_menu.isdigit():
            art_sub_menu = input("Please enter a digit that is 1 - 3: ").strip()
    
        # Checks if user entered a digit that is from 1-4
        while int(art_sub_menu) < 0 or int(art_sub_menu) > 3:
            art_sub_menu = input("Please enter any option from 1 - 3: ").strip()
        
        if art_sub_menu == '1':
            art()
        elif art_sub_menu == '2':
            main_menu()
        else:
            login()
            
    else:
        main_menu()
   
    
def update():
    ''' Update Function: updates any of the existing user's passwords'''
    print("\n1. Update Password\n2. Back to Main Menu\n")
    update_menu = input("Please choose any option from 1 - 2: ").strip()
        
    if update_menu == "1":
        print("\nUpdating Password\n")
        
        EmpID = input("Please enter the employee's 4 digit ID to begin update: ").strip()
        while not EmpID:
            EmpID = input("Employee ID cannot be blank. Please enter the employee's 4 digit ID to begin update: ")
        while not EmpID.isdigit():
            EmpID = input("Employee ID should consist of digits ONLY. Please enter the employee's 4 digit ID to begin update: ").strip()
        while len(EmpID) != 4:
                EmpID = input("Employee ID should consists of FOUR digits only. Please enter employee's 4 digit ID to begin update: ").strip()
        
        OldPass = input("Please enter your current your password: ").strip()
        while not OldPass:
                OldPass = input("Password cannot be blank. Please enter employee's current password: ").strip()
        with conn:
            cur = conn.cursor()
            try:    
                selectQuery = "SELECT COUNT (*) FROM Employee WHERE (EmployeeID = '" + EmpID + "'AND Password = '" + OldPass + "')"
                cur.execute(selectQuery)
                results = cur.fetchone()
            except:
                print("ERROR: Couldn't connect to database.")
#    
        # Checks if entered EmpID and OldPass are in the database
        # If not, provides error message and loops the update back until valid credentials
        while results[0] != 1:
            print("\nInvalid credentials. Please check your Employee ID/password again.\n")
            EmpID = input("Please enter the employee's 4 digit ID to begin update: ").strip()
            
            while not EmpID:
                EmpID = input("Employee ID cannot be blank. Please enter the employee's 4 digit ID to begin update: ")
            while not EmpID.isdigit():
                EmpID = input("Employee ID should consist of digits ONLY. Please enter the employee's 4 digit ID to begin update: ").strip()
            while len(EmpID) != 4:
                    EmpID = input("Employee ID should consists of FOUR digits only. Please enter employee's 4 digit ID to begin update: ").strip()
            
            OldPass = input("Please enter your current your password: ").strip()
            while not OldPass:
                    OldPass = input("Password cannot be blank. Please enter employee's current password: ").strip()
#                        
            with conn:
                cur = conn.cursor()
                try:    
                    selectQuery = "SELECT COUNT (*) FROM Employee WHERE (EmployeeID = '" + EmpID + "'AND Password = '" + OldPass + "')"
                    cur.execute(selectQuery)
                    results = cur.fetchone()
                except:
                    print("ERROR: Couldn't connect to database.")
                    
        NewPass = input("Please enter your new password: ").strip()
        while not NewPass:
                NewPass = input("Password cannot be blank. Please enter employee's desired new password: ").strip()
        
        ConfirmPass = input("Please confirm your new password: ").strip()
        while not ConfirmPass:
                ConfirmPass = input("Password confirmation cannot be blank. Please confirm new employee's password: ").strip()
        
        while NewPass != ConfirmPass:
            NewPass = input("Please enter your new password: ").strip()
            while not NewPass:
                NewPass = input("Password cannot be blank. Please enter employee's desired new password: ").strip()
        
            ConfirmPass = input("Please confirm your new password: ").strip()
            while not ConfirmPass:
                    ConfirmPass = input("Password confirmation cannot be blank. Please confirm new employee's password: ").strip()   
        
        with conn:
                cur = conn.cursor()
                try: 
                    UpdateValue = "UPDATE Employee SET Password = ('{}') WHERE (EmployeeID = ('{}') AND Password = ('{}'))"
                    UpdateString = UpdateValue.format(NewPass, EmpID, OldPass)
                    cur.execute(UpdateString)
                    cur.execute("SELECT * FROM Employee WHERE(EmployeeID = '{}')".format(EmpID))
                    updated_results = cur.fetchone()
                except:
                    print("ERROR: Couldn't connect to database.")
                    
        print("\nUpdate Successful!")
        print(updated_results)
        print("\n1. Update Another Employee\n2. Back to Main Menu\n3. Log Out\n")
        update_sub_menu = ("Please enter any option from 1 - 3: ")
        
        while not update_sub_menu:
            update_sub_menu = input("Input cannot be blank. Please enter a digit that is 1 - 3: ").strip()
        # Checks if user entered a digit
        while not update_sub_menu.isdigit():
            update_sub_menu = input("Please enter a digit that is 1 - 3: ").strip()
    
        # Checks if user entered a digit that is from 1-4
        while int(update_sub_menu) < 0 or int(update_sub_menu) > 3:
            update_sub_menu = input("Please enter any option from 1 - 3: ").strip()
        
        while int(update_sub_menu) == 1:
            print("\nUpdating Password\n")
        
            EmpID = input("Please enter the employee's 4 digit ID to begin update: ").strip()
            
            while not EmpID.isdigit():
                EmpID = input("Employee ID should consist of digits ONLY. Please enter the employee's 4 digit ID to begin update: ").strip()
            while len(EmpID) != 4:
                    EmpID = input("Employee ID should consists of FOUR digits only. Please enter employee's 4 digit ID to begin update: ").strip()
            
            OldPass = input("Please enter your current your password: ").strip()
            while not OldPass:
                    OldPass = input("Password cannot be blank. Please enter employee's current password: ").strip()
            
            selectQuery = "SELECT COUNT (*) FROM Employee WHERE (EmployeeID = '" + EmpID + "'AND Password = '" + OldPass + "')"
            cur.execute(selectQuery)
            results = cur.fetchone()
            
            # Checks if entered EmpID and OldPass are in the database
            # If not, provides error message and loops the update back until valid credentials
            while results[0] != 1:
                print("\nInvalid credentials. Please check your Employee ID/password again.\n")
                EmpID = input("Please enter the employee's 4 digit ID to begin update: ").strip()
                
                while not EmpID:
                    EmpID = input("Employee ID cannot be blank. Please enter the employee's 4 digit ID to begin update: ")
                while not EmpID.isdigit():
                    EmpID = input("Employee ID should consist of digits ONLY. Please enter the employee's 4 digit ID to begin update: ").strip()
                while len(EmpID) != 4:
                        EmpID = input("Employee ID should consists of FOUR digits only. Please enter employee's 4 digit ID to begin update: ").strip()
                
                OldPass = input("Please enter your current your password: ").strip()
                while not OldPass:
                        OldPass = input("Password cannot be blank. Please enter employee's current password: ").strip()
#                        
                selectQuery = "SELECT COUNT (*) FROM Employee WHERE (EmployeeID = '" + EmpID + "'AND Password = '" + OldPass + "')"
                cur.execute(selectQuery)
                results = cur.fetchone()
            
            NewPass = input("Please enter your new password: ").strip()
            while not NewPass:
                    NewPass = input("Password cannot be blank. Please enter employee's desired new password: ").strip()
            
            ConfirmPass = input("Please confirm your new password: ").strip()
            while not ConfirmPass:
                    ConfirmPass = input("Password confirmation cannot be blank. Please confirm new employee's password: ").strip()
            
            while NewPass != ConfirmPass:
                NewPass = input("Please enter your new password: ").strip()
                while not NewPass:
                    NewPass = input("Password cannot be blank. Please enter employee's desired new password: ").strip()
            
                ConfirmPass = input("Please confirm your new password: ").strip()
                while not ConfirmPass:
                        ConfirmPass = input("Password confirmation cannot be blank. Please confirm new employee's password: ").strip()
            
            UpdateValue = "UPDATE Employee SET Password = ('{}') WHERE (EmployeeID = ('{}') AND Password = ('{}'))"
            UpdateString = UpdateValue.format(NewPass, EmpID, OldPass)
            cur.execute(UpdateString)
            cur.execute("SELECT * FROM Employee WHERE(EmployeeID = '{}')".format(EmpID))
            updated_results = cur.fetchone()
            print("\nUpdate Successful!")
            print(updated_results)
            
            print("\n1. Update Another Employee\n2. Back to Main Menu\n3. Log Out\n")
            update_sub_menu = ("Please enter any option from 1 - 3: ")
            
            while not update_sub_menu:
                update_sub_menu = input("Input cannot be blank. Please enter a digit that is 1 - 3: ").strip()
            # Checks if user entered a digit
            while not update_sub_menu.isdigit():
                update_sub_menu = input("Please enter a digit that is 1 - 3: ").strip()
        
            # Checks if user entered a digit that is from 1-4
            while int(update_sub_menu) < 0 or int(update_sub_menu) > 3:
                update_sub_menu = input("Please enter any option from 1 - 3: ").strip()
            
        if int(update_sub_menu) == 2:
            main_menu()
        else:
            login()
        
    else:
        main_menu()

def register():
    ''' Register Function: registers any new employee into the database '''
    with conn:
        cur = conn.cursor()
        try:
            EmpID = input("Please enter new employee's desired 4 digit ID: ").strip()
            
            while not EmpID.isdigit():
                EmpID = input("Employee ID should consist of DIGITS only. Please enter new employee's desired 4 digit ID: ").strip()
            
            while len(EmpID) != 4:
                EmpID = input("Employee ID should consists of FOUR digits only. Please enter new employee's desired 4 digit ID: ").strip()
                
            cur.execute("SELECT COUNT (*) FROM Employee WHERE(EmployeeID = '" + EmpID + "')")
            results = cur.fetchone()
            
            while results[0] == 1 or not EmpID:
                EmpID = input("EmployeeID cannot be blank or repeated. Please enter new employee's desired 4 digit ID: ").strip()
                cur.execute("SELECT COUNT (*) FROM Employee WHERE(EmployeeID = '" + EmpID + "')")
                results = cur.fetchone()
                
            FName = input("Ready for new employee's first name: ").strip()
            while not FName:
                FName = input("First name cannot be blank. Please enter the employee's first name: ").strip()
            
            LName = input("Ready for new user's last name: ").strip()
            while not LName:
                LName = input("Last name cannot be blank. Please enter the employee's first name: ").strip()
            
            # Checks for correct email format
            Email = input("Ready for new user's email: ").strip()
            while not Email:
                Email = input("Email cannot be blank. Please enter new employee's email: ").strip()
            while not ("@" or ".edu" or ".com" or ".net" or ".org") in Email:
                Email = input("Email must contain an '...@___.com' or '...@___.edu' etc.. Please enter new employee's email: ").strip()
            
            # Checks for empty inputs
            Password = input("Ready for new user's desired password: ").strip()
            while not Password:
                Password = input("Password cannot be blank. Please enter new employee's password: ").strip()
            
            PassConfirm = input("Please confirm employee's password: ").strip()
            while not PassConfirm:
                PassConfirm = input("Password confirmation cannot be blank. Please confirm new employee's password: ").strip()
    
            # Confirms new user's password
            while PassConfirm != Password:
                print("\nPasswords did not match with confirmation. Try again.")
                Password = input("Please enter your password: ").strip()
                PassConfirm = input("Please confirm your password: ").strip()  
                
            InsertValue = "INSERT INTO Employee VALUES ('{}', '{}', '{}', '{}', '{}')"
            InsertString = InsertValue.format(EmpID, FName, LName, Email, Password)
            cur.execute(InsertString)
            cur.execute("SELECT * FROM Employee WHERE (EmployeeID = '{}')".format(EmpID))
            newEmp = cur.fetchone()
            print("\nRegistration Successful!")
            print(newEmp)
#    
            print("\n1. Register Another Employee\n2. Back to Main Menu\n3. Log Out\n")
            reg_sub_menu = ("Please enter any option from 1 - 3: ")
            
            while not reg_sub_menu:
                reg_sub_menu = input("Input cannot be blank. Please enter a digit that is 1 - 3: ").strip()
                
            # Checks if user entered a digit
            while not reg_sub_menu.isdigit():
                reg_sub_menu = input("Please enter a digit that is 1 - 3: ").strip()
        
            # Checks if user entered a digit that is from 1-4
            while int(reg_sub_menu) < 0 or int(reg_sub_menu) > 3:
                reg_sub_menu = input("Please enter any option from 1 - 3: ").strip()
            
            while int(reg_sub_menu) == 1:
                EmpID = input("Please enter new employee's desired 4 digit ID: ").strip()
            
                while not EmpID.isdigit():
                    EmpID = input("Employee ID should consist of DIGITS only. Please enter new employee's desired 4 digit ID: ").strip()
                
                while len(EmpID) != 4:
                    EmpID = input("Employee ID should consists of FOUR digits only. Please enter new employee's desired 4 digit ID: ").strip()
                    
                cur.execute("SELECT COUNT (*) FROM Employee WHERE(EmployeeID = '" + EmpID + "')")
                results = cur.fetchone()
                
                while results[0] == 1 or not EmpID:
                    EmpID = input("EmployeeID cannot be blank or repeated. Please enter new employee's desired 4 digit ID: ").strip()
                    cur.execute("SELECT COUNT (*) FROM Employee WHERE(EmployeeID = '" + EmpID + "')")
                    results = cur.fetchone()
                    
                FName = input("Ready for new employee's first name: ").strip()
                while not FName:
                    FName = input("First name cannot be blank. Please enter the employee's first name: ").strip()
                
                LName = input("Ready for new user's last name: ").strip()
                while not LName:
                    LName = input("Last name cannot be blank. Please enter the employee's first name: ").strip()
                
                # Checks for correct email format
                Email = input("Ready for new user's email: ").strip()
                while not Email:
                    Email = input("Email cannot be blank. Please enter new employee's email: ").strip()
                while not ("@" or ".edu" or ".com" or ".net" or ".org") in Email:
                    Email = input("Email must contain an '...@___.com' or '...@___.edu' etc.. Please enter new employee's email: ").strip()
                
                # Checks for empty inputs
                Password = input("Ready for new user's desired password: ").strip()
                while not Password:
                    Password = input("Password cannot be blank. Please enter new employee's password: ").strip()
                
                PassConfirm = input("Please confirm employee's password: ").strip()
                while not PassConfirm:
                    PassConfirm = input("Password confirmation cannot be blank. Please confirm new employee's password: ").strip()
        
                # Confirms new user's password
                while PassConfirm != Password:
                    print("\nPasswords did not match with confirmation. Try again.")
                    Password = input("Please enter your password: ").strip()
                    PassConfirm = input("Please confirm your password: ").strip()  
                    
                InsertValue = "INSERT INTO Employee VALUES ('{}', '{}', '{}', '{}', '{}')"
                InsertString = InsertValue.format(EmpID, FName, LName, Email, Password)
                cur.execute(InsertString)
                cur.execute("SELECT * FROM Employee WHERE (EmployeeID = '{}')".format(EmpID))
                newEmp = cur.fetchone()
                print("\nRegistration Successful!")
                print(newEmp)
    #    
                print("\n1. Register Another Employee\n2. Back to Main Menu\n3. Log Out\n")
                reg_sub_menu = ("Please enter any option from 1 - 3: ")
                
                while not reg_sub_menu:
                    reg_sub_menu = input("Input cannot be blank. Please enter a digit that is 1 - 3: ").strip()
                    
                # Checks if user entered a digit
                while not reg_sub_menu.isdigit():
                    reg_sub_menu = input("Please enter a digit that is 1 - 3: ").strip()
            
                # Checks if user entered a digit that is from 1-4
                while int(reg_sub_menu) < 0 or int(reg_sub_menu) > 3:
                    reg_sub_menu = input("Please enter any option from 1 - 3: ").strip()
                    
            if int(reg_sub_menu) == 2:
                main_menu()
            else:
                login()
        except:
            print("ERROR: Couldn't connect to database.")

def main_menu():
    ''' Post Login Function: allows user to have access to the business system after logging in.'''
    
    # Displays the Main Menu
    print("\n1. High-End Art Analysis\n2. Customer Loyalty Analysis\n3. Register New User\n4. Update Existing User\n5. Log Out")       
    decision = input("Please choose any option 1 - 5: ").strip()
    
    while not decision:
        decision = input("Input cannot be blank. Please enter a digit that is 1 - 5: ").strip()
                
    # Checks if user entered a digit
    while not decision.isdigit():
        decision = input("Please enter a digit that is 1 - 5: ").strip()
    
    # Checks if user entered a digit that is from 1-6
    while int(decision) < 0 or int(decision) > 5:
        decision = input("Please enter any option from 1 - 5: ").strip()
    
    # Redirects user to the selected menu from the display
    if decision == '1':
        art()
    elif decision == '2':
        customer_loyalty()
    elif decision == '3':
        register()
    elif decision == '4':
        update()
    else:
        login()
        
def login():
    ''' Login Function: used as our main function where everything begins. User logs into the system with their credentials via this system'''
    
    # Checks to ensure that user is using the proper format when entering in their email
    userEmail = input("Please enter your email to login: ").strip()
    while userEmail == "": 
        userEmail = input("Email cannot be blank, please enter your email to login: ").strip()
    while not ("@" or ".edu" or ".com" or ".net" or ".org") in userEmail:
        userEmail = input("Try again. Email must contain an '...@___.com' or '...@___.edu' etc. : ").strip()
    
    # Checks user to see if user had enter a password
    userPassword =  input("Please enter your password: ").strip()
    while not userPassword:
        userPassword = input("Password cannot be blank, please enter your password to login: ").strip()
    
    # Runs through the database and searches for an email/password match
    # If no match, loops user back to attempt login once again until pass
    with conn:
        cur = conn.cursor()
        try:
            selectQuery = "SELECT COUNT (*) FROM Employee WHERE (Email = '" + userEmail + "'AND Password = '" + userPassword + "')"
            cur.execute(selectQuery)
            results = cur.fetchone()
    
            # Checks if entered userEmail and Password are in the database
            # If not, provides error message and loops the login back until successful login
            while results[0] != 1:
                print("\nLogin unsuccessful. Please check your email/password again.\n")
                userEmail = input("Please enter your email to login: ").strip()
                while not userEmail: 
                    userEmail = input("Email cannot be blank, please enter your email to login: ").strip()
                    
                userPassword =  input("Please enter your password: ").strip()
                while not userPassword:
                    userPassword = input("Password cannot be blank, please enter your password to login: ").strip()
                    
                selectQuery = "SELECT COUNT (*) FROM Employee WHERE (Email = '" + userEmail + "'AND Password = '" + userPassword + "')"
                cur.execute(selectQuery)
                results = cur.fetchone()

        except:
            print("ERROR: Couldn't connect to database.")
        
        main_menu()

login()