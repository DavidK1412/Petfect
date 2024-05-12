from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from authApp.security.token_validator import validate_admin


from employeesApp.models.employee import Employee
from employeesApp.serializers.employeeSerializer import EmployeeSerializer
from employeesApp.models.speciality import Speciality


class EmployeeSpecialityView(generics.GenericAPIView):
    serializer_class = EmployeeSerializer
    permission_classes = (IsAuthenticated, )

    def post(self, request, *args, **kwargs):
        if not validate_admin(request.META.get('HTTP_AUTHORIZATION')[7:]):
            return Response({'error': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            employee = Employee.objects.get(pk=kwargs['pk'])
            if employee is None:
                return Response(status=status.HTTP_404_NOT_FOUND)
            for speciality in request.data['specialities']:
                temp = Speciality.objects.get(pk=speciality['id'])
                if temp is None:
                    return Response(status=status.HTTP_404_NOT_FOUND)
                employee.specialities.add(temp)
            serializer = EmployeeSerializer(employee, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save(employee=employee)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Employee.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, *args, **kwargs):
        if not validate_admin(request.META.get('HTTP_AUTHORIZATION')[7:]):
            return Response({'error': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            employee = Employee.objects.get(pk=kwargs['pk'])
            if employee is None:
                return Response(status=status.HTTP_404_NOT_FOUND)
            for speciality in request.data['specialities']:
                temp = Speciality.objects.get(pk=speciality['id'])
                if temp is None:
                    return Response(status=status.HTTP_404_NOT_FOUND)
                employee.specialities.remove(temp)
            serializer = EmployeeSerializer(employee, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save(employee=employee)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Employee.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
