import csv

def write_into_csv(info_list):
    with open("student_info.csv","a",newline='') as csvfile:
        writer = csv.writer(csv_file)
        if csvfile.tell() == 0:
            writer.writerow("Name","Age","Mob_No", "Email")

        writer.writerow(info_list)

if __name__ == '__main__':

    cond = True

    while(cond):

        stu_info = input(" Enter student information in this way (name age mob_no email")

        stu_info_list = stu_info.split(' ')
        print("Entered Information : "+str[stu_info_list])

        print("The information is  -\n Name{} \n Age{} \nMobile_Number{} \nEmail{}"
              .format(stu_info_list[0],stu_info_list[1],stu_info_list[2],stu_info_list[3]))

        choice = input("Entered Information is correct")

        if choice == "yes":
            write_into_csv(stu_info_list)

            cond_check = input("Enter yes to continue")
            if cond_check == "yes":
                cond = True
            elif cond_check == "no":
                cond = False

        elif choice == "no":
            print("Re-enter the values")



