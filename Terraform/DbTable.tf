resource "aws_dynamodb_table" "bas"{
  name           = "VisitorCounter"
  billing_mode   = "PROVISIONED"
  read_capacity  = 20
  write_capacity = 20
  hash_key       = "Site"
  range_key      = "Visitors"

attribute {
    name = "Site"
    type = "N"
  } 

  attribute {
    name = "Visits"
    type = "N"
  } 

  }
