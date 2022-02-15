import 'package:client/src/shared/widgets/shared_home_view_card.dart';
import 'package:flutter/material.dart';

class SharedGradeSelectorView extends StatefulWidget {
  const SharedGradeSelectorView({Key? key}) : super(key: key);

  @override
  _SharedGradeSelectorViewState createState() =>
      _SharedGradeSelectorViewState();
}

class _SharedGradeSelectorViewState extends State<SharedGradeSelectorView> {
  final _grades = [
    const SharedHomeViewCard(
      icon: Icons.folder,
      title: 'Form 1',
      routeTo: '',
    ),
    const SharedHomeViewCard(
      icon: Icons.folder,
      title: 'Form 2',
      routeTo: '',
    ),
    const SharedHomeViewCard(
      icon: Icons.folder,
      title: 'Form 3',
      routeTo: '',
    ),
    const SharedHomeViewCard(
      icon: Icons.folder,
      title: 'Form 4',
      routeTo: '',
    ),
    const SharedHomeViewCard(
      icon: Icons.folder,
      title: 'Form 5',
      routeTo: '',
    ),
    const SharedHomeViewCard(
      icon: Icons.folder,
      title: 'Form 6',
      routeTo: '',
    ),
  ];

  @override
  Widget build(BuildContext context) {
    return SafeArea(
      child: Scaffold(
        body: Padding(
          padding: const EdgeInsets.symmetric(vertical: 30),
          child: Column(
            children: [
              Text(
                'Choose your level',
                style: Theme.of(context).textTheme.headline4,
              ),
              const SizedBox(height: 30),
              Expanded(
                child: Padding(
                  padding: const EdgeInsets.all(8.0),
                  child: GridView.count(
                    crossAxisCount: 4,
                    children: _grades.map((e) => e).toList(),
                    mainAxisSpacing: 100,
                    crossAxisSpacing: 80,
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
