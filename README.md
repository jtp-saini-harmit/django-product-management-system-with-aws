# Product Management System

Django-based product management system running on AWS with CDK infrastructure.

## Project Structure

```
django-app/
├── product_management/    # Main Django project
├── products/             # Django app
├── scripts/              # Deployment scripts
├── Dockerfile           # Container definition
├── requirements.txt     # Python dependencies
├── buildspec.yml       # AWS CodeBuild config
└── appspec.yaml        # AWS CodeDeploy config
```

## Local Development

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate   # Windows
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create .env file:
```bash
DJANGO_SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_NAME=product_management
DATABASE_USER=admin
DATABASE_PASSWORD=your-password
DATABASE_HOST=localhost
DATABASE_PORT=5432
```

4. Run migrations:
```bash
python manage.py migrate
python manage.py createsuperuser
```

5. Run development server:
```bash
python manage.py runserver
```

## AWS Deployment

1. Configure AWS credentials:
```bash
aws configure
```

2. Deploy CDK stack:
```bash
cd ../cdk-infrastructure
npm install
cdk deploy MyArchitectureStackTokyo
```

3. Push code to repository:
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin <your-repo-url>
git push -u origin main
```

## Infrastructure

- VPC with public/private subnets
- RDS PostgreSQL with RDS Proxy
- ECS Fargate for containerized deployment
- Application Load Balancer
- CloudFront CDN
- CI/CD pipeline with CodePipeline
- Monitoring with CloudWatch

## API Endpoints

- `/api/categories/` - Product categories
- `/api/products/` - Product management
- `/api/customers/` - Customer data
- `/api/sales/` - Sales records
- `/api/sales/dashboard_stats/` - Sales statistics

## Monitoring

- CloudWatch dashboard: ProductManagementSystem
- Container logs: CloudWatch Logs
- Database metrics: RDS monitoring
- Application metrics: ECS Container Insights

## Security

- Secrets managed via AWS Secrets Manager
- RDS Proxy for secure database access
- WAF protection for ALB
- SSL/TLS encryption for all traffic
- VPC security groups for network isolation

## Maintenance

- Database backups: Automatic via RDS
- Log retention: CloudWatch Logs
- Infrastructure: AWS CDK
- Deployments: AWS CodePipeline

## Contributing

1. Create a feature branch
2. Make changes
3. Submit pull request
4. CI/CD pipeline will automatically deploy approved changes

## License

MIT
