# Office_Lunch_Order

This app help you to order lunch in your company simply way!

## Created models:
-   Restaurant with phone_regex
`Code` phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
