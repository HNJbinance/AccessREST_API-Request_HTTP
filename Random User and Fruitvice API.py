from randomuser import RandomUser
import pandas as pd

# First, we will create a random user object, r.
r = RandomUser()

# Then, using generate_users() function, we get a list of random 10 users.
some_list = r.generate_users(10)
print(some_list)

# an generate the required parameters to construct a dataset.
# For example, to get full name, we call get_full_name() function.

print(r.get_full_name())

# generate 10  full name
for user in some_list:
    print (user.get_full_name()," ",user.get_email())

# constructing a data set

def get_users():
    users = []

    for user in RandomUser.generate_users(10):
        users.append({"Name": user.get_full_name(), "Gender": user.get_gender(), "City": user.get_city(),
                      "State": user.get_state(), "Email": user.get_email(), "DOB": user.get_dob(),
                      "Picture": user.get_picture()})

    return pd.DataFrame(users)

df1 = pd.DataFrame(get_users())

print(df1)