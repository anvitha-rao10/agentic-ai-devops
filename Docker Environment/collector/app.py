def jenkins_watcher():
    global LAST_BUILD_PROCESSED

    while True:
        try:
            print("🔍 Checking Jenkins...")

            build = fetch_last_build()
            print("📦 Build:", build.get("number"), build.get("result"))

            build_number = build.get("number")

            if (
                build.get("result") == "FAILURE"
                and build_number != LAST_BUILD_PROCESSED
            ):
                print("🚨 Failure detected")

                log = fetch_console_log()

                event = {
                    "event_id": f"evt-{uuid.uuid4()}",
                    "timestamp": datetime.utcnow().isoformat() + "Z",
                    "source": "jenkins",
                    "ci": {
                        "job_name": build.get("fullDisplayName"),
                        "build_id": build_number
                    },
                    "error": {
                        "error_type": "GIT_SSH_FAILURE",
                        "raw_log": log[:1500]
                    }
                }

                EVENTS.append(event)
                LAST_BUILD_PROCESSED = build_number
                print("✅ Event stored")

        except Exception as e:
            print("❌ Watcher error:", e)

        time.sleep(10)
