import 'package:client/src/shared/services/fake_repo_service.dart';
import 'package:expandable/expandable.dart';
import 'package:flutter/material.dart';

class CourseContentView extends StatefulWidget {
  const CourseContentView({Key? key, this.args}) : super(key: key);

  /// receive course id
  final Map<String, dynamic>? args;

  @override
  State<CourseContentView> createState() => _CourseContentViewState();
}

class _CourseContentViewState extends State<CourseContentView> {
  String selectedSubTopic = '';

  void changeSubTopic(String val) {
    setState(() {
      selectedSubTopic = val;
    });
  }

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
          padding: const EdgeInsets.all(42.0),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text(
                'Course Content',
                style: Theme.of(context).textTheme.headline5,
              ),
              const SizedBox(height: 20),
              Text(
                FakeRepoService.courseDescription,
                style: Theme.of(context)
                    .textTheme
                    .subtitle1
                    ?.copyWith(color: Colors.grey),
              ),
              const SizedBox(height: 20),
              Expanded(
                child: Row(
                  children: [
                    Expanded(
                      flex: 2,
                      child: ListView(
                        children: [
                          ExpandablePanel(
                            header: const Text('Intro'),
                            collapsed: const Text('Intro to course'),
                            expanded: Column(
                              children: [
                                Container(
                                  height: 50,
                                  width: double.infinity,
                                  decoration: BoxDecoration(
                                    color: Colors.transparent,
                                    borderRadius: BorderRadius.circular(10),
                                  ),
                                  child: const Text('Who this is for?'),
                                ),
                                const Text('Topics to cover?'),
                                const Text('What you will learn'),
                              ],
                            ),
                          ),
                          ExpandablePanel(
                            header: const Text('Chapter 1'),
                            collapsed: const Text('Chapter outline'),
                            expanded: Column(
                              children: const [
                                Text('Who this is for?'),
                                Text('Topics to cover?'),
                                Text('What you will learn'),
                              ],
                            ),
                          ),
                          ExpandablePanel(
                            header: const Text('Chapter 2'),
                            collapsed: const Text('Chapter outline'),
                            expanded: Column(
                              children: const [
                                Text('Who this is for?'),
                                Text('Topics to cover?'),
                                Text('What you will learn'),
                              ],
                            ),
                          ),
                        ],
                      ),
                    ),
                    Expanded(
                      flex: 6,
                      child: Column(
                        children: const [
                          Text('Ola'),
                        ],
                      ),
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
