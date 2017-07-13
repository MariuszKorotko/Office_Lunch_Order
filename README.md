[Office Lunch Order](https://mariuszkorotko.github.io/Office_Lunch_Order/)

# Office_Lunch_Order
This app help you to order lunch in your company simply way!

### Models:
- Restaurant (phone_regex field).
- Dinner (relationship many-to-one with Restaurant)
- Order (relationship many-to-many through OrderedDinners model)
- OrderedDinners (relationship many-to-one with User, Dinner, Order models)

### Templates:


