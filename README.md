# codeshwar-test

# codeshwar-agent

GitHub OAuth + CodeShwar Integration Test

Prerequisites

    GitHub OAuth App credentials
    CodeShwar server running locally

Setup

    Set environment variables:
    bash

export CLIENT_ID="your_github_oauth_client_id"
export GITHUB_SECRET="your_github_oauth_secret"

Start CodeShwar server:
bash

# Navigate to your CodeShwar folder and start the server
cd path/to/codeshwar
# Follow CodeShwar's startup instructions
# Server should run on http://localhost:8000

Quick Start

    Start OAuth server:
    bash

python server.py

Server runs on http://127.0.0.1:8004

Run OAuth client:
bash

python client.py

    This will open GitHub OAuth in your browser

Flow Overview

    OAuth server handles GitHub authentication

    Client obtains access token via browser flow

    System automatically creates a GitHub issue

    CodeShwar processes the issue and generates code

File Structure

    server.py - OAuth server (port 8004)

    client.py - OAuth client interface

    issue.py - GitHub issue creation

    repo_details.py - Repository information

    query_details.py - Parse user queries

Testing

The complete flow:

    CodeShwar server running on port 8000 ✅

    OAuth server running on port 8004 ✅

    Run client.py to trigger OAuth flow ✅

    System creates issue and sends to CodeShwar ✅

    Note: CodeShwar must be running before starting the OAuth flow.
