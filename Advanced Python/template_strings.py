# LinkedIn Learning Course: Advanced Python by Joe Marini
# Demonstrate template string functions

from string import Template


def main():
    str1 = "You're watching {0} by {1}".format("Advanced Python", "Joe Marini")
    print(str1)

    # Create a template with a placeholder
    templ = Template("You're watching ${title} by ${author}")

    # Use the substitute method with keyword arguments
    str2 = templ.substitute(title="Advanced Python", author="Joe Marini")
    print(str2)

    # Use the substitute method with a dictionary
    data = {
        "author" : "Joe Marini",
        "title" : "Advanced Python"
    }
    str3 = templ.substitute(data)
    print(str3)
main()

