import random # To generate a random Application ID

# TELLING PYTHON PROJECT BRANCH AND ITS CUTOFFS
# Key = Branch Name, Value = Minimum Percentage Required
cutoffs = {"CSE (Computer Science)": 90.0,"AI & Data Science": 88.0,"ECE (Electronics)": 80.0,"MECH (Mechanical)": 70.0,"CIVIL (Civil Engg)": 60.0}

# --- 2. MAIN PROGRAM ---
print("*******************************************")
print("      WELCOME TO UNIVERSITY ADMISSIONS     ")
print("*******************************************")


while True:
    print("\n--- New Student Application ---")
    
    # 1. Get Student Details
    name = input("Enter Student Name: ")
    
    while True:
        try:
            perc = float(input(f"Enter 12th Grade Percentage for {name}: "))
            if 0 <= perc <= 100:
                break # Valid input, exit the small loop
            else:
                print(">> Error: Percentage must be between 0 and 100.")
        except ValueError:
            print(">> Error: Please enter a valid number.")

    print(f"\nProcessing application for {name}...")
    
    # --- 3. CHECK ELIGIBILITY ---
    # List to store branches
    eligible_branches = [] 
    
    # For Loop to check every branch in our dictionary
    for branch, min_marks in cutoffs.items():
        if perc >= min_marks:
            eligible_branches.append(branch)
    
    # --- 4. DECISION MAKING ---
    if len(eligible_branches) == 0:
        print("\nSORRY: Based on your marks, you are not eligible for any branch.")
        print("Better luck next time!")
        
    else:
        print(f"\nCONGRATULATIONS! You are eligible for {len(eligible_branches)} branches:")
        print("-" * 30)
        count = 1
        for item in eligible_branches:
            print(f"{count}. {item}")
            count += 1
        print("-" * 30)
        
        # Ask user to pick a seat
        choice = input("Type the name of the branch you want to finalize (or type 'cancel'): ")
        
        #check if they typed a valid eligible branch
        #use specific string matching here
        found = False
        for item in eligible_branches:
            if choice.lower() in item.lower():
                found = True
                app_id = random.randint(1000, 9999)
                print("\n" + "="*35)
                print(f" ADMISSION CONFIRMED")
                print("="*35)
                print(f" Name        : {name}")
                print(f" Branch      : {item}")
                print(f" Application ID: #UNI-{app_id}")
                print(f" Fee to Pay  : Rs. 75,000")
                print("="*35)
                break # Stop checking
        
        if not found:
            if choice.lower() != 'cancel':
                print("\n>> Selection failed. Please type the branch name exactly next time.")
            else:
                print("\n>> Application cancelled by user.")

    # --- 5. RESTART OR EXIT ---
    print("\n")
    next_step = input("Do you want to process another student? (yes/no): ")
    
    if next_step.lower() != "yes":
        print("\nExiting System. Have a nice day!")
        break # Breaks the main While loop