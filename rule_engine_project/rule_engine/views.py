import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import Rule


def index(request):
    rules = Rule.objects.all()  # Fetch all rules from the database
    return render(request, 'rule_engine/index.html', {'rules': rules})  # Pass rules to the template


@csrf_exempt
def create_rule_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        rule_string = data.get('rule', '')
        if rule_string:
            rule = Rule(rule_string=rule_string)
            rule.save()  # Save the rule to the database
            return JsonResponse({"success": True, "message": "Rule created successfully", "rule_id": rule.id})
        return JsonResponse({"success": False, "message": "Invalid rule"})


@csrf_exempt
def evaluate_rule_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_data = data.get('user_data', {})
        # Fetch all rules from the database
        rules = Rule.objects.all()
        evaluation_results = []

        for rule in rules:
            rule_string = rule.rule_string
            try:
                # Create a local context with user data
                local_context = {
                    'age': user_data.get('age', 0),
                    'department': user_data.get('department', ''),
                    'salary': user_data.get('salary', 0),
                    'experience': user_data.get('experience', 0)
                }

                # Debugging info
                print("Evaluating Rule:", rule_string)
                print("Local Context:", local_context)

                # Replace AND/OR with Python equivalents for evaluation
                python_rule = rule_string.replace('AND', 'and').replace('OR', 'or').replace('=', '==')

                # Evaluate the rule in the context of local_context
                rule_eval = eval(python_rule, {}, local_context)

                evaluation_results.append({"rule": rule_string, "result": rule_eval})

            except Exception as e:
                evaluation_results.append({"rule": rule_string, "result": f"Error evaluating rule: {str(e)}"})

        return JsonResponse({"results": evaluation_results})


