"""
Instrument aiopg to report a span for each executed Postgres queries::

    from ddtrace import patch
    from ddtrace.trace import Pin
    import aiopg

    # If not patched yet, you can patch aiopg specifically
    patch(aiopg=True)

    # This will report a span with the default settings
    async with aiopg.connect(DSN) as db:
        with (await db.cursor()) as cursor:
            await cursor.execute("SELECT * FROM users WHERE id = 1")

    # Use a pin to specify metadata related to this connection
    Pin.override(db, service='postgres-users')
"""
