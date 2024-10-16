# # # FileNotFound
# # try:
# #     file = open("a_file.txt")
# #     a_dictionary = {"key": "value"}
# #     print(a_dictionary["key"])
# # except FileNotFoundError:
# #     file = open("a_file.txt", "w")
# #     file.write("something")
# # except KeyError as error_message:
# #     print(f"The key {error_message} does not exist.")
# # else:
# #     content = file.read()
# #     print(content)
# # finally:
# #     # file.close()
# #     # print("File was closed.")
# #     raise TypeError
# #
# height = float(input("Height: "))
# weight = int(input("Weight: "))
#
# if height > 3:
#     raise ValueError("Human Height should not over 3 meters.")
# bmi = weight / height ** 2
#
# # print(bmi)
#
# fruits = ["Apple", "Pear", "Orange"]
#
# # Catch the exception and make sure the code runs without crashing.
#
#
# try:
#     def make_pie(index):
#         fruit = fruits[index]
#         print(fruit + " pie")
#
#
#     print(make_pie(4))
# except IndexError:
#     result = "Fruit pie."
#     print(result)

facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]


def count_likes(posts):
    total_likes = 0
    for post in posts:
        try:
            total_likes + post['Likes']
        except KeyError:
            pass
        else:
            total_likes = total_likes + post['Likes']

    return total_likes


print(count_likes(facebook_posts))
