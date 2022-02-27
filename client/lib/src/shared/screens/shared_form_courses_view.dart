import 'package:client/src/shared/widgets/course_card.dart';
import 'package:flutter/material.dart';

class SharedFormCoursesView extends StatelessWidget {
  const SharedFormCoursesView({
    Key? key,
    this.args,
  }) : super(key: key);

  final Map<String, dynamic>? args;

  @override
  Widget build(BuildContext context) {
    return SafeArea(
      child: Scaffold(
        appBar: AppBar(
          leading: IconButton(
            onPressed: () {
              Navigator.pop(context);
            },
            icon: const Icon(Icons.arrow_back),
          ),
        ),
        body: Padding(
          padding: const EdgeInsets.all(45.0),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text(
                'All Live Courses [8]',
                style: Theme.of(context).textTheme.headline5,
              ),
              const SizedBox(height: 30),
              Expanded(
                child: GridView.count(
                  crossAxisCount: 3,
                  mainAxisSpacing: 90,
                  crossAxisSpacing: 100,
                  children: const [
                    CourseCard(
                      name: 'Biology',
                      topics: 3,
                    ),
                    CourseCard(
                      name: 'Chemistry',
                      topics: 17,
                    ),
                    CourseCard(
                      name: 'Maths',
                      topics: 23,
                    ),
                    CourseCard(
                      name: 'Shona',
                      topics: 11,
                    ),
                    CourseCard(
                      name: 'Fashion & Fabrics',
                      topics: 14,
                    ),
                    CourseCard(
                      name: 'Agriculture',
                      topics: 16,
                    ),
                    CourseCard(
                      name: 'French',
                      topics: 7,
                    ),
                    CourseCard(
                      name: 'Metal Work',
                      topics: 34,
                    ),
                  ],
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
