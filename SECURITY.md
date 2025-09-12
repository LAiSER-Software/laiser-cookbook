# Security Policy

## Supported Versions

We actively support the latest version of LAiSER Cookbook. Since this is a collection of educational notebooks, we recommend always using the most recent version.

| Version | Supported          |
| ------- | ------------------ |
| Latest  | ✅ |
| Older   | ❌ |

## Reporting a Vulnerability

If you discover a security vulnerability in LAiSER Cookbook, please report it responsibly:

### For Critical Security Issues
- **Email**: Contact the maintainers directly through the repository's contact information
- **Do not**: Open a public issue for critical security vulnerabilities
- **Include**: Detailed description, steps to reproduce, and potential impact

### For Non-Critical Issues
- **GitHub Issues**: Use the issue tracker for non-sensitive security concerns
- **Label**: Use the "security" label when creating the issue

## Security Considerations

### API Keys and Credentials
- **Never commit**: API keys, tokens, or credentials to the repository
- **Use environment variables**: Store sensitive information securely
- **Notebook safety**: Always use input prompts or environment variables for credentials in notebooks

### Data Privacy
- **Sample data**: Ensure all sample datasets contain only public or anonymized information
- **User data**: Provide clear guidance on handling sensitive user data
- **Privacy by design**: Encourage best practices for data handling in all recipes

### Dependencies
- **Package security**: We regularly review dependencies for known vulnerabilities
- **Updates**: Keep the LAiSER package and other dependencies updated
- **Verification**: Only use packages from trusted sources

## Best Practices for Users

When using LAiSER Cookbook:

1. **Protect credentials**: Never hardcode API keys or tokens
2. **Secure environments**: Use secure notebook environments
3. **Data handling**: Follow your organization's data handling policies
4. **Regular updates**: Keep packages updated to receive security patches

## Response Timeline

- **Initial response**: Within 48 hours of reporting
- **Assessment**: Within 1 week for security impact evaluation
- **Resolution**: Timeline depends on severity and complexity

## Disclosure Policy

We follow responsible disclosure practices:
- Issues are addressed before public disclosure
- Credit is given to reporters (unless they prefer anonymity)
- Updates are communicated through appropriate channels

Thank you for helping keep LAiSER Cookbook secure!