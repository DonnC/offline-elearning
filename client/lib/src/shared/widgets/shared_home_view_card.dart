import 'package:client/src/constants/index.dart';
import 'package:flutter/material.dart';
import 'package:styled_widget/styled_widget.dart';

class SharedHomeViewCard extends StatelessWidget {
  const SharedHomeViewCard({
    Key? key,
    required this.icon,
    required this.title,
    required this.routeTo,
  }) : super(key: key);

  final IconData icon;
  final String title;
  final String routeTo;

  @override
  Widget build(BuildContext context) {
    return SizedBox(
      height: 300,
      width: 300,
      child: Card(
        color: AppColors.whiteColor,
        child: GestureDetector(
          onTap: () {
            Navigator.pushReplacementNamed(context, routeTo);
          },
          child: Center(
            child: Column(
              mainAxisAlignment: MainAxisAlignment.spaceAround,
              children: [
                Icon(icon).iconColor(AppColors.buttonBgColor).iconSize(120),
                Text(
                  title,
                  style: Theme.of(context).textTheme.headline6,
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
