# https://www.hackerearth.com/practice/algorithms/greedy/basics-of-greedy-algorithms/practice-problems/algorithm/eat-or-not-22/

class EatOrNot(object):

  def __init__(self):
    pass

  def get_user_input(self):
    vitamins_required, carbohydrates_required, fats_required, proteins_required = [int(number) for number in input().split()]
    number_of_fruits = int(input())
    fruit_details = list(list())
    for counter in range(0, number_of_fruits):
      fruit_details.append([int(number) for number in input().split()])
    self.set_input(vitamins_required, carbohydrates_required, fats_required, proteins_required, number_of_fruits, fruit_details)

  def set_input(self, vitamins_required, carbohydrates_required, fats_required, proteins_required, number_of_fruits, fruit_details):
    self.vitamins_required = vitamins_required
    self.carbohydrates_required = carbohydrates_required
    self.fats_required = fats_required
    self.proteins_required = proteins_required
    self.number_of_fruits = number_of_fruits
    self.fruit_details = fruit_details
    self.nutrient_name_to_required_mapping = {
      'vitamins': vitamins_required,
      'carbohydrates': carbohydrates_required,
      'fats': fats_required,
      'proteins': proteins_required
    }

  def can_monk_get_fit(self):
    if (self.can_monk_get_right_amount_of_nutrients(0, 'vitamins') and \
    self.can_monk_get_right_amount_of_nutrients(1, 'carbohydrates')  and \
    self.can_monk_get_right_amount_of_nutrients(2, 'fats')  and \
    self.can_monk_get_right_amount_of_nutrients(3, 'proteins')):
      return "YES"
    return "NO"

  def can_monk_get_right_amount_of_nutrients(self, nutrient_detail_position, nutrient_name):
    nutrient_details = list()
    for counter in range(0, self.number_of_fruits):
      nutrient_details.append(self.fruit_details[counter][nutrient_detail_position])
    return self.is_subset_sum(self.number_of_fruits, nutrient_details, self.nutrient_name_to_required_mapping[nutrient_name])

  def is_subset_sum(self, number_of_elements, elements, sum):
    if sum == 0:
      return True
    elif ((sum > 0 and number_of_elements == 0) or sum < 0):
      return False
    return self.is_subset_sum(number_of_elements-1, elements[:-1], sum) or self.is_subset_sum(number_of_elements-1, elements[:-1], sum-elements[-1])

if __name__ == '__main__':
  eat_or_not = EatOrNot()
  eat_or_not.get_user_input()
  print (eat_or_not.can_monk_get_fit())