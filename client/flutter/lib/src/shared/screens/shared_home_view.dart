import 'package:client/src/constants/index.dart';
import 'package:client/src/shared/widgets/shared_home_view_card.dart';
import 'package:flutter/material.dart';

class SharedHomeView extends StatefulWidget {
  const SharedHomeView({Key? key}) : super(key: key);

  @override
  _SharedHomeViewState createState() => _SharedHomeViewState();
}

class _SharedHomeViewState extends State<SharedHomeView> {
  @override
  Widget build(BuildContext context) {
    return SafeArea(
      child: Scaffold(
        body: Padding(
          padding: const EdgeInsets.symmetric(vertical: 100),
          child: Column(
            children: [
              Text(
                'I am a',
                style: Theme.of(context).textTheme.headline4,
              ),
              const SizedBox(height: 30),
              Expanded(
                child: Padding(
                  padding: const EdgeInsets.all(8.0),
                  child: Row(
                    mainAxisAlignment: MainAxisAlignment.spaceAround,
                    children: const [
                      SharedHomeViewCard(
                        icon: Icons.person,
                        title: 'Student',
                        routeTo: sharedGradeSelector,
                      ),
                      SharedHomeViewCard(
                        icon: Icons.school,
                        title: 'Teacher',
                        routeTo: '',
                      ),
                      SharedHomeViewCard(
                        icon: Icons.admin_panel_settings,
                        title: 'Admin',
                        routeTo: '',
                      ),
                    ],
                  ),
                ),
              ),
              const SizedBox(height: 30),
              Text(
                'Offline eLearning Sys - 2022 @DonnC N0173320W',
                style: Theme.of(context).textTheme.subtitle2?.copyWith(
                    fontStyle: FontStyle.italic, fontWeight: FontWeight.w400),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
