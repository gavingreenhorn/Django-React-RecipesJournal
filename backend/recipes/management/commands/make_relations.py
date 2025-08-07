import os
from random import randint, sample

from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model
from django.conf import settings
from recipes.models import Tag, Ingredient, Recipe, Component

from ._utils import get_image

User = get_user_model()


class Command(BaseCommand):
    def handle(self, *args, **options):
        img_dir = 'media/recipes/images'
        image_count = len(os.listdir(img_dir))
        user_count = User.objects.count()
        all_tags = list(Tag.objects.values_list('pk', flat=True))
        all_ingredients = list(Ingredient.objects.values_list('pk', flat=True))
        test_recipes_amount = 6
        test_tags_amount = 3
        test_ingredients_amount = 5
        try:
            for i in range(0, test_recipes_amount):
                img_path = os.path.join(
                    settings.BASE_DIR,
                    f'{img_dir}/{i % image_count + 1}.jpg')
                recipe = Recipe.objects.create(
                    author_id=randint(1, user_count),
                    name=f"test_recipe_{i + 1}",
                    cooking_time=randint(1, 60), image=get_image(img_path)
                )
                tags = Tag.objects.filter(
                    pk__in=sample(all_tags, test_tags_amount))
                ingredients = Ingredient.objects.filter(
                    pk__in=sample(
                        all_ingredients, test_ingredients_amount
                    )
                )
                recipe.tags.add(*tags)
                for ingredient in ingredients:
                    Component.objects.create(
                        recipe=recipe, ingredient=ingredient,
                        amount=randint(10, 400))
        except Exception as ex:
            raise CommandError(ex)
        else:
            self.stdout.write(self.style.SUCCESS(
                'Successfully created recipe objects'))
