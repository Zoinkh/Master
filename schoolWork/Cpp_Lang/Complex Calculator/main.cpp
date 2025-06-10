#include <iostream>
#include <string>
#include <cmath>

using namespace std;

bool isPrime(int n) {
    if (n <= 1)
        return false;

    for (int i = 2; i <= sqrt(n); ++i) {
        if (n % i == 0)
            return false;
    }

    return true;
}

bool isEven(int n) {
    return (n % 2 == 0);
}

bool isOdd(int n) {
    return (n % 2 != 0);
}

bool isPerfect(int n) {
    int sum = 1;
    for (int i = 2; i <= n / 2; ++i) {
        if (n % i == 0)
            sum += i;
    }
    return (sum == n);
}

int factorial(int n) {
    if (n <= 1)
        return 1;
    return n * factorial(n - 1);
}

int fibonacci(int n) {
    if (n <= 0)
        return 0;
    if (n == 1)
        return 1;

    int prev = 0;
    int curr = 1;

    for (int i = 2; i <= n; ++i) {
        int next = prev + curr;
        prev = curr;
        curr = next;
    }

    return curr;
}

string decimalToBinary(int num) {
    string binary;
    while (num > 0) {
        binary = to_string(num % 2) + binary;
        num /= 2;
    }
    return binary;
}

int binaryToDecimal(const string& binary) {
    int decimal = 0;
    int power = 0;
    for (int i = binary.length() - 1; i >= 0; --i) {
        if (binary[i] == '1')
            decimal += pow(2, power);
        power++;
    }
    return decimal;
}

string decimalToHexadecimal(int num) {
    string hexadecimal;
    while (num > 0) {
        int remainder = num % 16;
        if (remainder < 10)
            hexadecimal = to_string(remainder) + hexadecimal;
        else
            hexadecimal = static_cast<char>(remainder - 10 + 'A') + hexadecimal;
        num /= 16;
    }
    return hexadecimal;
}

int hexadecimalToDecimal(const string& hexadecimal) {
    int decimal = 0;
    int power = 0;
    for (int i = hexadecimal.length() - 1; i >= 0; --i) {
        if (hexadecimal[i] >= '0' && hexadecimal[i] <= '9')
            decimal += (hexadecimal[i] - '0') * pow(16, power);
        else if (hexadecimal[i] >= 'A' && hexadecimal[i] <= 'F')
            decimal += (hexadecimal[i] - 'A' + 10) * pow(16, power);
        power++;
    }
    return decimal;
}

string binaryToHexadecimal(const string& binary) {
    int decimal = binaryToDecimal(binary);
    return decimalToHexadecimal(decimal);
}

string hexadecimalToBinary(const string& hexadecimal) {
    int decimal = hexadecimalToDecimal(hexadecimal);
    return decimalToBinary(decimal);
}

string decimalToOctal(int num) {
    string octal;
    while (num > 0) {
        octal = to_string(num % 8) + octal;
        num /= 8;
    }
    return octal;
}

int octalToDecimal(const string& octal) {
    int decimal = 0;
    int power = 0;
    for (int i = octal.length() - 1; i >= 0; --i) {
        decimal += (octal[i] - '0') * pow(8, power);
        power++;
    }
    return decimal;
}

string binaryToOctal(const string& binary) {
    int decimal = binaryToDecimal(binary);
    return decimalToOctal(decimal);
}

string octalToBinary(const string& octal) {
    int decimal = octalToDecimal(octal);
    return decimalToBinary(decimal);
}

string hexadecimalToOctal(const string& hexadecimal) {
    int decimal = hexadecimalToDecimal(hexadecimal);
    return decimalToOctal(decimal);
}

string octalToHexadecimal(const string& octal) {
    int decimal = octalToDecimal(octal);
    return decimalToHexadecimal(decimal);
}

int main() {
    int num1, num2;
    int operation;
    char performAnother;

    cout << "Scientific Calculator\n\n";

    std::cout << "\033[32m";

    do {
        cout << "Enter the first number: ";
        cin >> num1;
        cout << "Available operations:\n";
        cout << "1. Addition\n";
        cout << "2. Subtraction\n";
        cout << "3. Multiplication\n";
        cout << "4. Division\n";
        cout << "5. Modulo\n";
        cout << "6. Power\n";
        cout << "7. Square\n";
        cout << "8. Cube\n";
        cout << "9. Square root (sqrt)\n";
        cout << "10. Exponentiation (exp)\n";
        cout << "11. Natural logarithm (ln)\n";
        cout << "12. Logarithm base 10 (log10)\n";
        cout << "13. Sine (sin)\n";
        cout << "14. Cosine (cos)\n";
        cout << "15. Tangent (tan)\n";
        cout << "16. Arcsine (asin)\n";
        cout << "17. Arccosine (acos)\n";
        cout << "18. Arctangent (atan)\n";
        cout << "19. Hyperbolic sine (sinh)\n";
        cout << "20. Hyperbolic cosine (cosh)\n";
        cout << "21. Hyperbolic tangent (tanh)\n";
        cout << "22. Factorial\n";
        cout << "23. Check if Prime (Number 1)\n";
        cout << "24. Check if Prime (Number 2)\n";
        cout << "25. Check if Even (Number 1)\n";
        cout << "26. Check if Even (Number 2)\n";
        cout << "27. Check if Odd (Number 1)\n";
        cout << "28. Check if Odd (Number 2)\n";
        cout << "29. Check if Perfect (Number 1)\n";
        cout << "30. Check if Perfect (Number 2)\n";
        cout << "31. Fibonacci (Number 1)\n";
        cout << "32. Fibonacci (Number 2)\n";
        cout << "33. Decimal to Binary (Number 1)\n";
        cout << "34. Decimal to Binary (Number 2)\n";
        cout << "35. Binary to Decimal (Number 1)\n";
        cout << "36. Binary to Decimal (Number 2)\n";
        cout << "37. Decimal to Hexadecimal (Number 1)\n";
        cout << "38. Decimal to Hexadecimal (Number 2)\n";
        cout << "39. Hexadecimal to Decimal (Number 1)\n";
        cout << "40. Hexadecimal to Decimal (Number 2)\n";
        cout << "41. Binary to Hexadecimal (Number 1)\n";
        cout << "42. Binary to Hexadecimal (Number 2)\n";
        cout << "43. Hexadecimal to Binary (Number 1)\n";
        cout << "44. Hexadecimal to Binary (Number 2)\n";
        cout << "45. Decimal to Octal (Number 1)\n";
        cout << "46. Decimal to Octal (Number 2)\n";
        cout << "47. Octal to Decimal (Number 1)\n";
        cout << "48. Octal to Decimal (Number 2)\n";
        cout << "49. Binary to Octal (Number 1)\n";
        cout << "50. Binary to Octal (Number 2)\n";
        cout << "51. Octal to Binary (Number 1)\n";
        cout << "52. Octal to Binary (Number 2)\n";
        cout << "53. Hexadecimal to Octal (Number 1)\n";
        cout << "54. Hexadecimal to Octal (Number 2)\n";
        cout << "55. Octal to Hexadecimal (Number 1)\n";
        cout << "56. Octal to Hexadecimal (Number 2)\n";
        cout << "\nEnter the operation number: ";
        cin >> operation;
        cout << "Enter the second number: ";
        cin >> num2;

        switch (operation) {
            case 1: {
                int result = num1 + num2;
                cout << "Addition: " << num1 << " + " << num2 << " = " << result << "\n";
                break;
            }
            case 2: {
                int result = num1 - num2;
                cout << "Subtraction: " << num1 << " - " << num2 << " = " << result << "\n";
                break;
            }
            case 3: {
                int result = num1 * num2;
                cout << "Multiplication: " << num1 << " * " << num2 << " = " << result << "\n";
                break;
            }
            case 4: {
                if (num2 != 0) {
                    double result = static_cast<double>(num1) / num2;
                    cout << "Division: " << num1 << " / " << num2 << " = " << result << "\n";
                } else {
                    cout << "Division by zero is not allowed!\n";
                }
                break;
            }
            case 5: {
                if (num2 != 0) {
                    int result = num1 % num2;
                    cout << "Modulo: " << num1 << " % " << num2 << " = " << result << "\n";
                } else {
                    cout << "Modulo by zero is not allowed!\n";
                }
                break;
            }
            case 6: {
                int result = pow(num1, num2);
                cout << "Power: " << num1 << " ^ " << num2 << " = " << result << "\n";
                break;
            }
            case 7: {
                int result = num1 * num1;
                cout << "Square of " << num1 << " = " << result << "\n";
                break;
            }
            case 8: {
                int result = num1 * num1 * num1;
                cout << "Cube of " << num1 << " = " << result << "\n";
                break;
            }
            case 9: {
                if (num1 >= 0) {
                    double result = sqrt(num1);
                    cout << "Square root of " << num1 << " = " << result << "\n";
                } else {
                    cout << "Square root operation is only defined for non-negative numbers.\n";
                }
                break;
            }
            case 10: {
                double result = exp(num1);
                cout << "Exponentiation of " << num1 << " = " << result << "\n";
                break;
            }
            case 11: {
                if (num1 > 0) {
                    double result = log(num1);
                    cout << "Natural logarithm of " << num1 << " = " << result << "\n";
                } else {
                    cout << "Natural logarithm operation is only defined for positive numbers.\n";
                }
                break;
            }
            case 12: {
                if (num1 > 0) {
                    double result = log10(num1);
                    cout << "Logarithm base 10 of " << num1 << " = " << result << "\n";
                } else {
                    cout << "Logarithm base 10 operation is only defined for positive numbers.\n";
                }
                break;
            }
            case 13: {
                double result = sin(num1);
                cout << "Sine of " << num1 << " = " << result << "\n";
                break;
            }
            case 14: {
                double result = cos(num1);
                cout << "Cosine of " << num1 << " = " << result << "\n";
                break;
            }
            case 15: {
                double result = tan(num1);
                cout << "Tangent of " << num1 << " = " << result << "\n";
                break;
            }
            case 16: {
                double result = asin(num1);
                cout << "Arcsine of " << num1 << " = " << result << "\n";
                break;
            }
            case 17: {
                double result = acos(num1);
                cout << "Arccosine of " << num1 << " = " << result << "\n";
                break;
            }
            case 18: {
                double result = atan(num1);
                cout << "Arctangent of " << num1 << " = " << result << "\n";
                break;
            }
            case 19: {
                double result = sinh(num1);
                cout << "Hyperbolic sine of " << num1 << " = " << result << "\n";
                break;
            }
            case 20: {
                double result = cosh(num1);
                cout << "Hyperbolic cosine of " << num1 << " = " << result << "\n";
                break;
            }
            case 21: {
                double result = tanh(num1);
                cout << "Hyperbolic tangent of " << num1 << " = " << result << "\n";
                break;
            }
            case 22: {
                if (num1 >= 0 && num1 == static_cast<int>(num1)) {
                    int n = static_cast<int>(num1);
                    int result = factorial(n);
                    cout << "Factorial of " << n << " = " << result << "\n";
                } else {
                    cout << "Factorial operation is only defined for non-negative integers.\n";
                }
                break;
            }
            case 23: {
                bool result = isPrime(num1);
                cout << num1 << " is " << (result ? "prime" : "not prime") << "\n";
                break;
            }
            case 24: {
                bool result = isPrime(num2);
                cout << num2 << " is " << (result ? "prime" : "not prime") << "\n";
                break;
            }
            case 25: {
                bool result = isEven(num1);
                cout << num1 << " is " << (result ? "even" : "odd") << "\n";
                break;
            }
            case 26: {
                bool result =isEven(num2);
                cout << num2 << " is " << (result ? "even" : "odd") << "\n";
                break;
            }
            case 27: {
                bool result = isOdd(num1);
                cout << num1 << " is " << (result ? "odd" : "even") << "\n";
                break;
            }
            case 28: {
                bool result = isOdd(num2);
                cout << num2 << " is " << (result ? "odd" : "even") << "\n";
                break;
            }
            case 29: {
                bool result = isPerfect(num1);
                cout << num1 << " is " << (result ? "a perfect number" : "not a perfect number") << "\n";
                break;
            }
            case 30: {
                bool result = isPerfect(num2);
                cout << num2 << " is " << (result ? "a perfect number" : "not a perfect number") << "\n";
                break;
            }
            case 31: {
                int result = fibonacci(num1);
                cout << "Fibonacci of " << num1 << " = " << result << "\n";
                break;
            }
            case 32: {
                int result = fibonacci(num2);
                cout << "Fibonacci of " << num2 << " = " << result << "\n";
                break;
            }
            case 33: {
                string result = decimalToBinary(num1);
                cout << "Decimal to Binary conversion of " << num1 << " = " << result << "\n";
                break;
            }
            case 34: {
                string result = decimalToBinary(num2);
                cout << "Decimal to Binary conversion of " << num2 << " = " << result << "\n";
                break;
            }
            case 35: {
                int result = binaryToDecimal(to_string(num1));
                cout << "Binary to Decimal conversion of " << num1 << " = " << result << "\n";
                break;
            }
            case 36: {
                int result = binaryToDecimal(to_string(num2));
                cout << "Binary to Decimal conversion of " << num2 << " = " << result << "\n";
                break;
            }
            case 37: {
                string result = decimalToHexadecimal(num1);
                cout << "Decimal to Hexadecimal conversion of " << num1 << " = " << result << "\n";
                break;
            }
            case 38: {
                string result = decimalToHexadecimal(num2);
                cout << "Decimal to Hexadecimal conversion of " << num2 << " = " << result << "\n";
                break;
            }
            case 39: {
                int result = hexadecimalToDecimal(to_string(num1));
                cout << "Hexadecimal to Decimal conversion of " << num1 << " = " << result << "\n";
                break;
            }
            case 40: {
                int result = hexadecimalToDecimal(to_string(num2));
                cout << "Hexadecimal to Decimal conversion of " << num2 << " = " << result << "\n";
                break;
            }
            case 41: {
                string result = binaryToHexadecimal(to_string(num1));
                cout << "Binary to Hexadecimal conversion of " << num1 << " = " << result << "\n";
                break;
            }
            case 42: {
                string result = binaryToHexadecimal(to_string(num2));
                cout << "Binary to Hexadecimal conversion of " << num2 << " = " << result << "\n";
                break;
            }
            case 43: {
                string result = hexadecimalToBinary(to_string(num1));
                cout << "Hexadecimal to Binary conversion of " << num1 << " = " << result << "\n";
                break;
            }
            case 44: {
                string result = hexadecimalToBinary(to_string(num2));
                cout << "Hexadecimal to Binary conversion of " << num2 << " = " << result << "\n";
                break;
            }
            case 45: {
                string result = decimalToOctal(num1);
                cout << "Decimal to Octal conversion of " << num1 << " = " << result << "\n";
                break;
            }
            case 46: {
                string result = decimalToOctal(num2);
                cout << "Decimal to Octal conversion of " << num2 << " = " << result << "\n";
                break;
            }
            case 47: {
                int result = octalToDecimal(to_string(num1));
                cout << "Octal to Decimal conversion of " << num1 << " = " << result << "\n";
                break;
            }
            case 48: {
                int result = octalToDecimal(to_string(num2));
                cout << "Octal to Decimal conversion of " << num2 << " = " << result << "\n";
                break;
            }
            case 49: {
                string result = binaryToOctal(to_string(num1));
                cout << "Binary to Octal conversion of " << num1 << " = " << result << "\n";
                break;
            }
            case 50: {
                string result = binaryToOctal(to_string(num2));
                cout << "Binary to Octal conversion of " << num2 << " = " << result << "\n";
                break;
            }
            case 51: {
                string result = octalToBinary(to_string(num1));
                cout << "Octal to Binary conversion of " << num1 << " = " << result << "\n";
                break;
            }
            case 52: {
               string result = octalToBinary(to_string(num2));
                cout << "Octal to Binary conversion of " << num2 << " = " << result << "\n";
                break;
            }
            case 53: {
                string result = hexadecimalToOctal(to_string(num1));
                cout << "Hexadecimal to Octal conversion of " << num1 << " = " << result << "\n";
                break;
            }
            case 54: {
                string result = hexadecimalToOctal(to_string(num2));
                cout << "Hexadecimal to Octal conversion of " << num2 << " = " << result << "\n";
                break;
            }
            case 55: {
                string result = octalToHexadecimal(to_string(num1));
                cout << "Octal to Hexadecimal conversion of " << num1 << " = " << result << "\n";
                break;
            }
            case 56: {
                string result = octalToHexadecimal(to_string(num2));
                cout << "Octal to Hexadecimal conversion of " << num2 << " = " << result << "\n";
                break;
            }
            default:
                cout << "Invalid operation!\n";
                break;
        }

        cout << "\nPerform another operation? (y/n): ";
        cin >> performAnother;
        cout << "\n";

    } while (performAnother == 'y' || performAnother == 'Y');

    cout << "Calculator program terminated.\n";

    return 0;
}
