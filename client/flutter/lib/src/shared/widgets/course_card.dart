import 'package:client/src/constants/index.dart';
import 'package:client/src/shared/models/index.dart';
import 'package:flutter/material.dart';

class CourseCard extends StatelessWidget {
  const CourseCard(
      {Key? key,
      required this.name,
      this.image = '',
      this.topics = 0,
      this.teachers = const []})
      : super(key: key);
  final String image;
  final int topics;
  final String name;
  final List<Teacher> teachers;

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: () {
        // TODO pass course id
        Navigator.pushNamed(context, courseContentScreen);
      },
      child: Card(
        elevation: 15,
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Container(
              width: double.infinity,
              height: 200,
              color: AppColors.getRandomColor(),
            ),
            const SizedBox(height: 15),
            Padding(
              padding: const EdgeInsets.all(16.0),
              child: Text('$topics Topics',
                  style: Theme.of(context)
                      .textTheme
                      .subtitle1
                      ?.copyWith(color: Colors.grey)),
            ),
            Padding(
              padding: const EdgeInsets.all(16.0),
              child: Text(name, style: Theme.of(context).textTheme.headline6),
            ),
          ],
        ),
      ),
    );
  }
}
