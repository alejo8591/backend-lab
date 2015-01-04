<?php

// Composer: "fzaninotto/faker": "v1.3.0"
use Faker\Factory as Faker;

class NewsTableSeeder extends Seeder
{

	public function run()
	{
		$faker = Faker::create();

		foreach(range(1, 18) as $index)
		{
			News::create(array(
				'title' => $faker->sentence($nbWords = 6),
				'content' => $faker->paragraph($nbSentences = 4),
				'active' => $faker->boolean
			));
		}
	}

}
