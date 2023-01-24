# General Description
- Excercise / Project comes originally from requirements for enrollment for DevOps Academy which took place in Kraków  organized by company GlobalLogic 

<br> 

# Exercise description
As a customer, I would like to buy a product from the shop

<br>

Given I’m a customer

Given the current state of <product> in shop is <initial_amount>

When I buy <buy_amount> <product>

Then the number of products in the warehouse is updated to <final_state>

<br> 

## Examples:
  /product/initial_amount/buy_amount/final_state/
  /orange/13/10/3/
  /apple/55/15/40/
  /apple/55/15/40/

<br> 

## Acceptance Criteria
- Implement an API for buying products,
- Implement an API for checking the status in the shop.

<br> 

## Mandatory requirements
- Publishing the code on GitHub on a public repository,
- History of git commits with incremental changes that prove individual effort,
- Object-Oriented Programming style,
- Python style convention - PEP8, https://peps.python.org/pep-0008/,
- Correctly designing the interface of classes or methods and python modules,
- Unit tests,
- Command-line interface,
- The state of the shop can be persisted in a JSON file, whenever a user wants to check the state of the shop, the shop is reading the file and extracting proper values, when a user buys something the shop modifies the file,
- README.md file with instructions about how to run the project.

<br> 

## It will be an asset if you:
- Add another complexity with a warehouse that is selling products to the shop. The shop is calculating the price with 30% commission. A product in a warehouse can have various prices from which the shop is buying a given amount of the product. When a customer wants to buy some amount of product, the shop needs to calculate what would be the price of that product based on prices in the warehouse. The order of product packages in the warehouse is fixed, eg. if we have 10 apples at price $5, 15 at price $2, and 5 at price $5 then we’re not optimizing the prices but selling it in the fixed order,
- Using flask and implementing REST API,
- Designing tests for flask application,
- Packaging the project (setup.py script) with instructions on how to do that,
- Docker image and instruction on how to run the application using docker image,
- Using GitHub Actions - https://docs.github.com/en/actions/quickstart.