def create_christmas_tree(height):
    for i in range(1, height + 1):
        spaces = " " * (height - i)
        tree_body = "*" * (2 * i - 1)
        print(f"{spaces}{tree_body}")

    trunk_width = height // 3
    trunk_spaces = " " * ((2 * height - trunk_width) // 2)
    for _ in range(height // 2):
        print(f"{trunk_spaces}{'|' * trunk_width}")

# Set the height of the Christmas tree
tree_height = 5

# Create and display the Christmas tree
create_christmas_tree(tree_height)
